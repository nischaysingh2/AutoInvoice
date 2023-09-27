import os
import random
from tkinter import *
from reportlab.pdfgen import canvas

class InvoiceGenerator:
    def __init__(self, bill):
        self.bill = bill
        self.bill.title("Nischay's Invoice Generator")
        self.bill.geometry("800x600")

        self.frame = Frame(self.bill, bg="white")
        self.frame.pack(fill='both', expand=True, padx=20, pady=20)

        title_label = Label(self.frame, text="Invoice Generator", font=("Arial", 30, "bold"), bg="white", fg="green")
        title_label.pack(pady=(0, 20))

        entry_frame = Frame(self.frame, bg="white")
        entry_frame.pack(fill='both', expand=True)

        labels = ["Invoice No.", "Date", "Customer Name", "Contact No", "Item Name", "Price", "Quantity"]
        self.entry_vars = {}

        for label in labels:
            label_frame = Frame(entry_frame, bg="white")
            label_frame.pack(fill='both', expand=True)

            label_widget = Label(label_frame, text=label, font=("Arial", 15, "bold"), bg="white", fg="gray")
            label_widget.pack(side=LEFT, padx=(0, 20))

            entry_var = StringVar()
            entry_widget = Entry(label_frame, textvariable=entry_var, font=("Arial", 15), bg="light grey")
            entry_widget.pack(fill='both', expand=True)
            self.entry_vars[label] = entry_var

        submit_button = Button(self.frame, text="Generate Invoice", command=self.generate_invoice, font=("Arial", 14),
                               fg="white", cursor="hand2", bg="#B00857")
        submit_button.pack(pady=(20, 0))

    def calculate(self):
        price = float(self.entry_vars["Price"].get())
        qty = float(self.entry_vars["Quantity"].get())
        return price * qty

    def gst(self):
        cal = self.calculate()
        tax_rate = 0.18
        tax_amount = cal * tax_rate
        total = cal + tax_amount
        return tax_amount, total

    def generate_invoice(self):
        invoice_no = self.entry_vars["Invoice No."].get()
        date = self.entry_vars["Date"].get()
        customer_name = self.entry_vars["Customer Name"].get()
        contact_no = self.entry_vars["Contact No"].get()
        item_name = self.entry_vars["Item Name"].get()
        price = self.entry_vars["Price"].get()
        quantity = self.entry_vars["Quantity"].get()
        tax_amount, total = self.gst()

        c = canvas.Canvas(f"Invoice_{invoice_no}.pdf", pagesize=(600, 800), bottomup=0)
        c.setFillColorRGB(0.6, 0.5, 0.8)

        # Draw invoice details, calculations, and any other desired content
        c.setFont("Arial", 10)
        c.drawString(50, 650, f"Invoice No.: {invoice_no}")
        c.drawString(50, 630, f"Date: {date}")
        c.drawString(50, 610, f"Customer Name: {customer_name}")
        c.drawString(50, 590, f"Contact No: {contact_no}")

        c.setFont("Arial", 12)
        c.drawString(50, 540, "Product Details:")
        c.drawString(50, 520, f"Item Name: {item_name}")
        c.drawString(50, 500, f"Price: {price}")
        c.drawString(50, 480, f"Quantity: {quantity}")

        c.setFont("Arial", 14)
        c.drawString(450, 430, f"Subtotal: {self.calculate():.2f}")
        c.drawString(450, 410, f"Tax Rate (18%): {self.gst()[0]:.2f}")
        c.drawString(450, 390, f"Tax Amount: {tax_amount:.2f}")
        c.drawString(450, 370, f"Total: {total:.2f}")

        c.drawString(50, 320, "Thank you for your business!")

        c.showPage()
        c.save()

def main():
    bill = Tk()
    obj = InvoiceGenerator(bill)
    bill.mainloop()

if __name__ == "__main__":
    main()
