import sqlite3
from django.shortcuts import render, redirect, reverse
from .models.tea import Tea
from .views.connection import Connection
from .models.model_factory import model_factory

# Create your views here.

def tea_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Tea)
            db_cursor = conn.cursor()
            
            db_cursor.execute('''
            SELECT *
            FROM teaapp_tea
            ORDER BY name;
            ''')
            
            all_tea = db_cursor.fetchall()
            print("ALL TEA!!!!", all_tea)