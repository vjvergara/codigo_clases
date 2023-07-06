import openai
from pydantic import BaseModel

openai.organization = 'org-qvjzo6Cm1uTTyH9422nbtwUQ'
openai.api_key = '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'


class Document(BaseModel):
    item: str = 'Profesor'


def process_inference(user_prompt) -> str:
    print('[PROCESANDO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres un profesor de programación experto. Vas a resolver cualquier duda de forma facil de entender para tus estudiantes
        E.G
        ¿Cuantos lenguajes de programación existen?
        
        Respuesta:
        C, C++, Java, Python, JavaScript
        """},
            {"role": "user", "content": user_prompt}
        ]
    )
    response = completion.choices[0].message.content
    return response
