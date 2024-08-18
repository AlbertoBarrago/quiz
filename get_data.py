import requests
import json


class QuestionDataService:
    def __init__(self, argument, length_value, language, difficulty, ollama_url="http://localhost:11434"):
        self.ollama_url = ollama_url
        self.arguments = {
            "argument": argument,
            "length": int(length_value),
            "language": language,
            "difficulty": difficulty,
        }

    def generate_question_data(self):
        question_data_value = []
        question = self._generate_question()
        question_data_value.append(question)
        return question_data_value

    def _generate_question(self):
        prompt = (f"Number of questions to generate: {self.arguments['length']}. "
                  f"Kind of questions: A true/false questions with its answer and a detailed explanation. "
                  f"Format the response as JSON with keys 'text', 'answer', and 'long_answer'. "
                  f"Format the response simple without wrapping nothing i read code processing response as 'text', 'answer', and 'long_answer'. "
                  f"The question should be related to {self.arguments['argument']}. "
                  f"The difficulty of the questions should be {self.arguments['difficulty']}. "
                  f"In this language {self.arguments['language']}")
        print(f"\nWe are generating the questions... 🚀"
              f"please be patient the process can take a few minutes.\n")
        response = self._query_ollama(prompt)
        try:
            json_str = response['response']
            start = json_str.find('[') if '[' in json_str else json_str.find('{')
            end = json_str.rfind(']') + 1 if ']' in json_str else json_str.rfind('}') + 1
            questions_json = json.loads(json_str[start:end])

            if isinstance(questions_json, list):
                return questions_json
            elif isinstance(questions_json, dict) and 'questions' in questions_json:
                return questions_json['questions']
            else:
                return questions_json
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            print(f"Error processing response: {e}")
            return []

    def _query_ollama(self, prompt):
        payload = {
            "model": "llama3.1",
            "prompt": prompt,
            "stream": False,
            "response_format": "json"
        }
        response = requests.post(f"{self.ollama_url}/api/generate", json=payload)
        return response.json()

