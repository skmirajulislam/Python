import tkinter as tk
from tkinter import filedialog
from pdf2docx import Converter

class PDFtoDOCXConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF to DOCX Converter")

        # Variables
        self.pdf_file_path = tk.StringVar()
        self.docx_file_path = tk.StringVar()

        # Labels
        tk.Label(root, text="PDF File:").grid(row=0, column=0, sticky="e", padx=10, pady=10)
        tk.Label(root, text="DOCX File:").grid(row=1, column=0, sticky="e", padx=10, pady=10)

        # Entry Widgets
        tk.Entry(root, textvariable=self.pdf_file_path, width=40).grid(row=0, column=1, padx=10, pady=10)
        tk.Entry(root, textvariable=self.docx_file_path, width=40).grid(row=1, column=1, padx=10, pady=10)

        # Browse Buttons
        tk.Button(root, text="Browse", command=self.browse_pdf).grid(row=0, column=2, padx=5, pady=10)
        tk.Button(root, text="Browse", command=self.browse_docx).grid(row=1, column=2, padx=5, pady=10)

        # Convert Button
        tk.Button(root, text="Convert", command=self.convert_pdf_to_docx).grid(row=2, column=1, pady=20)

    def browse_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.pdf_file_path.set(file_path)

    def browse_docx(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("DOCX Files", "*.docx")])
        if file_path:
            self.docx_file_path.set(file_path)

    def convert_pdf_to_docx(self):
        pdf_path = self.pdf_file_path.get()
        docx_path = self.docx_file_path.get()

        if pdf_path and docx_path:
            try:
                converter = Converter(pdf_path)
                converter.convert(docx_path)
                converter.close()
                tk.messagebox.showinfo("Conversion Successful", "PDF to DOCX conversion completed successfully!")
            except Exception as e:
                tk.messagebox.showerror("Conversion Error", f"An error occurred: {str(e)}")
        else:
            tk.messagebox.showwarning("File Paths Missing", "Please provide paths for both PDF and DOCX files.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFtoDOCXConverterApp(root)
    root.mainloop()
