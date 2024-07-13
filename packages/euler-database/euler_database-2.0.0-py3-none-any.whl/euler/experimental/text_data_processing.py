from pydantic import BaseModel, Field
import spacy
import os
import google.generativeai as genai
from euler.graph_api import KnowledgeGraphAPI
from euler.relationship import RelationshipManager
from euler.llm_reader.google_gemini_reader import GeminiProReader
from typing import List

class TextDataProcessing(BaseModel):
    openai_api_key: str = Field(default=None, description="Pass API key")

    def extract_relationships(self, input_text) -> List[str]:
        gemini_pro_reader = GeminiProReader(api_key=self.openai_api_key)
        result = gemini_pro_reader.read(input_text)

        if result is not None:
            print("Gemini Pro Output:", result.text)
            relationships = [rel.strip() for rel in result.text.split("\n") if "->" in rel]
            return relationships
        else:
            print("Failed to get output from Gemini Pro.")
            return []

    def text_convert_to_graph(self, chunks: str):
        nlp = spacy.load("en_core_web_sm")
        text = chunks
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        print(entities)
        relationships = self.extract_relationships(text)
        print("--relationships--", relationships)
        kg_api = KnowledgeGraphAPI()
        relationship_manager = RelationshipManager(kg_api.graph)

        for entity, label in entities:
            kg_api.create_node(entity, label)

        for relationship in relationships:
            source_target, rel = relationship.split("[")
            source, target = source_target.split("->")
            print(source, target, rel)
            relationship_manager.create_relationship(source.strip(), target.strip(), rel.strip(' ]'))

        # kg_api.visualize_graph('graph.png')
        graph_json = kg_api.get_graph_json()
        print(graph_json)


# Sample test 
#  text_data_processing.text_convert_to_graph(sample_text)












































    # def extarct_relationships(self, text):
    #     try:
    #         os.environ['GOOGLE_API_KEY'] = self.openai_api_key
    #         genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
    #     except Exception as e:
    #         print(f"[EXC]: Exception occurred due to API key. Check API Keys. {e}")

    #     try:
    #         prompt = f"Extract relationships between entities in the following text:\n\n{text}\n\nProvide the relationships in the format: Source -> Target [Relationship]"
    #         response = genai.GenerativeModel('models/gemini-pro').generate_content(prompt)
    #         print("response --", response.text)
    #         relationships_text = response.text.strip()
    #         relationships = relationships_text.split('\n')
    #         return [rel.split('[') for rel in relationships]
    #     except Exception as e:
    #         print(f"[EXC]: Exception occurred while extracting relationships. {e}")