{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNuuQu4npbXS4W2T51jlIOX"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3gvaRfZR8HmN",
        "outputId": "70d84ba6-2d2f-4e59-90b4-61189bb28fe8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Магазины в которых нет соли: {'Лента', 'Пятёрочка', 'Перекрёсток'}\n",
            "Магазины в которых можно купить молоко, печенье и сыр сразу: {'Лента', 'Магнит', 'Перекрёсток'}\n",
            "Магазины в которых можно купить мясо: {'Пятёрочка'}\n",
            "Магазины в которых можно купить молоко: {'Лента', 'Магнит', 'Пятёрочка', 'Перекрёсток'}\n"
          ]
        }
      ],
      "source": [
        "# Вариант 11.\n",
        "# В магазинах имеются следующие товары. Магнит – молоко, соль, сахар, печенье, сыр.\n",
        "# Пятерочка – мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар, печенье. Лента\n",
        "# – печенье, молоко, сыр.\n",
        "# Определить:\n",
        "# 1. в каких магазинах нельзя приобрести соль.\n",
        "# 2. в каких магазинах можно приобрести одновременно молоко, печенье и сыр.\n",
        "# 3. в каких магазинах можно приобрести мясо и молоко.\n",
        "\n",
        "\n",
        "\n",
        "magnet = {'молоко', 'соль', 'сахар', 'печенье', 'сыр'}\n",
        "pyatero4ka = {'мясо', 'молоко', 'сыр'}\n",
        "perekrestok = {'молоко', 'творог', 'сыр', 'сахар', 'печенье'}\n",
        "lenta = {'печенье', 'молоко', 'сыр'}\n",
        "\n",
        "\n",
        "notsol = set()\n",
        "mps = set()\n",
        "myaso = set()\n",
        "moloko = set()\n",
        "\n",
        "if 'соль' not in magnet:\n",
        "    notsol.add('Магнит')\n",
        "if 'соль' not in pyatero4ka:\n",
        "    notsol.add('Пятёрочка')\n",
        "if 'соль' not in perekrestok:\n",
        "    notsol.add('Перекрёсток')\n",
        "if 'соль' not in lenta:\n",
        "    notsol.add('Лента')\n",
        "\n",
        "if ('молоко' in magnet) and ('печенье' in magnet) and ('сыр' in magnet):\n",
        "    mps.add('Магнит')\n",
        "if ('молоко' in pyatero4ka) and ('печенье' in pyatero4ka) and ('сыр' in pyatero4ka):\n",
        "    mps.add('Пятёрочка')\n",
        "if ('молоко' in perekrestok) and ('печенье' in perekrestok) and ('сыр' in perekrestok):\n",
        "    mps.add('Перекрёсток')\n",
        "if ('молоко' in lenta) and ('печенье' in lenta) and ('сыр' in lenta):\n",
        "    mps.add('Лента')\n",
        "\n",
        "if 'мясо' in magnet:\n",
        "    myaso.add('Магнит')\n",
        "if 'мясо' in pyatero4ka:\n",
        "    myaso.add('Пятёрочка')\n",
        "if 'мясо' in perekrestok:\n",
        "    myaso.add('Перекрёсток')\n",
        "if 'мясо' in lenta:\n",
        "    myaso.add('Лента')\n",
        "\n",
        "if 'молоко' in magnet:\n",
        "    moloko.add('Магнит')\n",
        "if 'молоко' in pyatero4ka:\n",
        "    moloko.add('Пятёрочка')\n",
        "if 'молоко' in perekrestok:\n",
        "    moloko.add('Перекрёсток')\n",
        "if 'молоко' in lenta:\n",
        "    moloko.add('Лента')\n",
        "\n",
        "\n",
        "print(f'Магазины в которых нет соли: {notsol}')\n",
        "print(f'Магазины в которых можно купить молоко, печенье и сыр сразу: {mps}')\n",
        "print(f'Магазины в которых можно купить мясо: {myaso}')\n",
        "print(f'Магазины в которых можно купить молоко: {moloko}')"
      ]
    }
  ]
}