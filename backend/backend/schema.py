import graphene
import graphql_jwt
import api.schema

class Query(
    api.schema.Query
    ):
    pass


class Mutation(
    graphene.ObjectType
    ):
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema=graphene.Schema(query=Query,
                       mutation=Mutation,
                       )