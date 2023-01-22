{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "37a6b76e",
   "metadata": {},
   "source": [
    "### Funções para o jogo da Forca"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "272b5656",
   "metadata": {},
   "outputs": [],
   "source": [
    "def getWords():\n",
    "    \n",
    "    with open(r\"C:\\workspace\\palavras_jogoForca.txt\", mode=\"r\", encoding=\"utf-8\") as file:\n",
    "    \n",
    "        words_updated = []\n",
    "        words = file.readlines()\n",
    "        i = 0\n",
    "    \n",
    "        while(i < len(words)):           \n",
    "            words_updated.append(words[i].strip(\" \\n\"))\n",
    "            i += 1\n",
    "                    \n",
    "    file.close()    \n",
    "    return words_updated\n",
    "\n",
    "\n",
    "def getAttemptUser(word_chosen):\n",
    "        \n",
    "    char = input(\"Informe uma letra: \")\n",
    "    hasChar = False\n",
    "        \n",
    "    for el in word_chosen:\n",
    "        if el == char:\n",
    "            hasChar = True\n",
    "                \n",
    "    return char"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
