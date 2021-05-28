from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import datetime
from apps.expenses.models import Expense
from apps.income.models import Income


class ExpenseSummaryStats(APIView):

    def get_category(self, expense):
        return expense.category

    def get_amount_for_category(self, expense_list, category):
        expenses = expense_list.filter(category=category)
        amount = 0

        for expense in expenses:
            amount += expense.amount

        return {'amount': str(amount)}

    def get(self, request):
        # pega a date de hoje
        todays_date = datetime.date.today()
        # pega até um ano atrás da data de hoje
        ayear_ago = todays_date - datetime.timedelta(days=30 * 12)
        # pega todas as expenses do ultimo ano até o atual
        expenses = Expense.objects.filter(owner=request.user, date__gte=ayear_ago, date__lte=todays_date)

        final = {}
        # percorre um map retornando apenas o tipo de categoria unica nāo duplica
        categories = list(set(map(self.get_category, expenses)))

        # realiza um for dentro dos expenses achados pela query do banco
        for expense in expenses:
            # percorre o tipo de categoria encontrada no expense retornando do banco
            for category in categories:
                # cria uma tag da category encontrada e retorna o valor de toda category com o range de 1 ano
                final[category] = self.get_amount_for_category(expenses, category)

        return Response({'category_data': final}, status=status.HTTP_200_OK)


class IncomeSourcesSummaryStats(APIView):

    def get_source(self, income):
        return income.source

    def get_amount_for_source(self, income_list, source):
        incomes = income_list.filter(source=source)
        amount = 0

        for income in incomes:
            amount += income.amount

        return {'amount': str(amount)}

    def get(self, request):
        # pega a date de hoje
        todays_date = datetime.date.today()
        # pega até um ano atrás da data de hoje
        ayear_ago = todays_date - datetime.timedelta(days=30 * 12)
        # pega todas as expenses do ultimo ano até o atual
        income = Income.objects.filter(owner=request.user, date__gte=ayear_ago, date__lte=todays_date)

        final = {}
        # percorre um map retornando apenas o tipo de categoria unica nāo duplica
        sources = list(set(map(self.get_source, income)))

        # realiza um for dentro dos expenses achados pela query do banco
        for i in income:
            # percorre o tipo de categoria encontrada no expense retornando do banco
            for source in sources:
                # cria uma tag da category encontrada e retorna o valor de toda category com o range de 1 ano
                final[source] = self.get_amount_for_source(income, source)

        return Response({'income_source_data': final}, status=status.HTTP_200_OK)