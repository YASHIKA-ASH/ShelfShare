from app.ai.recommender import create_embedding

vector = create_embedding(
    "Operating System Concepts"
)

print(vector)
print(len(vector))