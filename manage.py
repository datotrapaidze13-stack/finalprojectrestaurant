#!/usr/bin/env python
"""Django-ს ბრძანებების ფაილი: ტერმინალის ბრძანებებს (runserver, migrate) Django-ს გადასცემს"""
import os
import sys


def main():
    """ტერმინალის ბრძანების შესრულება"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django ვერ მოიძებნა. შეამოწმე, დაყენებულია თუ არა "
            "და გააქტიურებულია თუ არა .venv"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
