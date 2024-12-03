import tkinter as tk
from openai import OpenAI


#client = OpenAI(api_key=)


def get_response(event=None):
    userinput = entry.get()  # Get the input from the Entry widget
    messages = [{"role": "system", "content": "You are a very helpful math tutor."},
                {"role": "user", "content": userinput}]

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    tutor_outputs = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": tutor_outputs})

    # Display the response in the output label
    output_label.config(text=tutor_outputs)

# Create the main window
root = tk.Tk()

# Set the title of the window
root.title("AI Tutor")

# Set the size and position of the window (positioned in the top-left corner)
root.geometry("400x300+0+0")  # Width x Height + X position + Y position

# back
root.configure(bg="#1E90FF")  # Dodger blue color

# Create a label with a blue background and white text
label = tk.Label(root, text="Enter your question:", bg="#1E90FF", fg="white", font=("Helvetica", 14, "bold"))
label.pack(pady=10)

# Create an entry widget (input field) with a white background and blue text
entry = tk.Entry(root, width=40, bg="white", fg="#1E90FF", font=("Helvetica", 12))
entry.pack(pady=10)

# Bind the Enter key to the get_response function
entry.bind("<Return>", get_response)

# Create a button with a white background and blue text
submit_button = tk.Button(root, text="Submit", command=get_response, bg="white", fg="#1E90FF", font=("Helvetica", 12, "bold"))
submit_button.pack(pady=10)

# frame
output_frame = tk.Frame(root, bg="white", highlightbackground="#1E90FF", highlightcolor="#1E90FF", highlightthickness=2)
output_frame.pack(pady=20, fill="both", expand=True, padx=20)

# label
output_label = tk.Label(output_frame, text="", wraplength=350, bg="white", fg="#1E90FF", font=("Helvetica", 12))
output_label.pack(padx=10, pady=10)

# run
root.mainloop()
