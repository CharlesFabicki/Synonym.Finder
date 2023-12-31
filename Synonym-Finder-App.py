import nltk
from nltk.corpus import wordnet
import tkinter as tk
from tkinter import messagebox, scrolledtext

nltk.download('wordnet')


class SynonymFinderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Synonym Finder")

        self.label = tk.Label(root, text="Enter a word:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Find Synonyms", command=self.find_synonyms)
        self.button.pack()

        self.output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, width=50)
        self.output_text.pack()

    def find_synonyms(self):
        word = self.entry.get().strip()

        if not word:
            messagebox.showwarning("Warning", "Please enter a word.")
            return

        if not wordnet.synsets(word):
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f"No synonyms found for '{word}'.")
            return

        synonyms = self.get_synonyms(word)

        self.output_text.delete(1.0, tk.END)
        for i, synset in enumerate(synonyms):
            synonyms_text = ", ".join(synset)
            self.output_text.insert(tk.END, f"Synonyms {i+1} of '{word}': {synonyms_text}\n")

    def get_synonyms(self, word):
        synonyms = []
        for syn in wordnet.synsets(word):
            synonyms.append([lemma.name() for lemma in syn.lemmas()])

            # Find hypernyms (more general terms)
            for hypernym in syn.hypernyms():
                synonyms.append([lemma.name() for lemma in hypernym.lemmas()])

            # Find hyponyms (more specific terms)
            for hyponym in syn.hyponyms():
                synonyms.append([lemma.name() for lemma in hyponym.lemmas()])

        return synonyms


if __name__ == "__main__":
    root = tk.Tk()
    app = SynonymFinderApp(root)
    root.mainloop()
