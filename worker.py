# profanity_check_minimal.py
import requests
import json


class ProfanityChecker:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def check_text(self, task, decision):
        print(f"Проверяем: '{decision}'")

        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=self.headers,
                json={
                    "model": "deepseek/deepseek-v3.2",
                    "messages": [
                        {
                            "role": "system",
                            "content": """Ты проверяешь задание по программированию у школьника, определи есть ли ошибки и напиши пояснение. 
                            Отвечай строго в формате JSON:
                            {"has_mistake": true/false, "mark": 0-10, 
                             "reason": "объяснение"}"""
                        },
                        {
                            "role": "user",
                            "content": f"Проанализируй решение: '{decision}', вот задание: '{task}'"
                        }
                    ]
                },
                timeout=15
            )

            response.raise_for_status()  # Проверяем на ошибки HTTP

            data = response.json()
            ai_response = data["choices"][0]["message"]["content"]

            try:
                start = ai_response.find('{')
                end = ai_response.rfind('}') + 1
                if start != -1 and end != 0:
                    json_str = ai_response[start:end]
                    result = json.loads(json_str)
                else:
                    result = {"has_mistake": True,
                              "mark": 0,
                              "reason": "что-то пошло не так 998"
                              }

            except json.JSONDecodeError:
                result = {"has_mistake": True,
                          "mark": 0,
                          "reason": "что-то пошло не так 999"
                          }

            return {
                **result,
                "raw_response": ai_response[:100] + "..." if len(ai_response) > 100 else ai_response
            }

        except requests.exceptions.RequestException as e:
            print(f"Ошибка сети: {e}")
            return {
                "has_mistake": True,
                "mark": 0,
                "reason": "что-то пошло не так 997"
            }

        except Exception as e:
            print(f"Неизвестная ошибка: {e}")
            return {
                "has_mistake": True,
                "mark": 0,
                "reason": "что-то пошло не так 996"
            }
