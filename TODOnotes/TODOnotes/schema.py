import graphene

from graphene_django import DjangoObjectType

from todo.models import Project, ToDo
from usersapp.models import CustomUser


class UserObjectType(DjangoObjectType):
    class Meta:
        model = CustomUser
        # fields = ('pk', 'username', 'first_name', 'last_name', 'email')
        fields = '__all__'


class TodoObjectType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class ProjectObjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class Query (graphene.ObjectType):

    all_users = graphene.List(UserObjectType)

    all_todo = graphene.List(TodoObjectType)

    all_projects = graphene.List(ProjectObjectType)

    get_todo_by_param = graphene.Field(TodoObjectType)


    def resolve_all_users (self, info):
        return CustomUser.objects.all()

    def resolve_all_todo (self, info):
        return ToDo.objects.all()

    def resolve_all_projects (self, info):
        return Project.objects.all()

    def resolve_get_todo_by_param (self, info):
        todo = ToDo.objects.all()
        return todo.filter(created_user=1)


class TodoMutation (graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        todo_body = graphene.String()

    todo = graphene.Field(TodoObjectType)

    @classmethod
    def mutate(cls, self, info, todo_body, id):
        todo = ToDo.objects.get(pk=id)
        todo.todo_body = todo_body
        todo.save()
        return TodoMutation(todo=todo)


class Mutation:
    update_todo = TodoMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
