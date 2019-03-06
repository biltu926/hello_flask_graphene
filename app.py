import json
import graphene
from flask import Flask, request
from flask_graphql import GraphQLView

app = Flask(__name__)


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.Argument(graphene.String, default_value="Stranger"),
                            age=graphene.Argument(graphene.Int))

    def resolve_hello(self, info, **args):
        return 'Hello {} your age is {}'.format(args['name'], args['age'])

schema = graphene.Schema(query=Query)

@app.route("/", methods=['POST'])
def hello():
    data = json.loads(request.data)
    print(data['query'])
    return json.dumps(schema.execute(data['query']).data)

if __name__ == "__main__":
    app.run(debug=True)
