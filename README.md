
# 🧠 Dataset Transformer Tool

An interactive Python tool for applying common data preprocessing transformations to CSV datasets. Built with a mix of `tkinter` and `CLI` for hands-on control.

---

## ✨ Features

✅ Impute missing values  
✅ Scale numerical data  
✅ Encode categorical features  
✅ Apply log/sqrt transforms  
✅ Bin or bucketize columns  
✅ Save transformed datasets easily

---

## 🎮 How to Use

Run this in a terminal:
```bash
python transformer_main.py
```

### You'll be guided to:
1. Select a dataset file (`CSV`,`XML`,`PARQUET`,`JSON`)
2. Choose transformation options from a menu
3. Apply and preview results
4. Save your transformed dataset wherever you want

---

## 🛠️ Dependencies

Install the required libraries (and your own modules) with:

```bash
pip install -r requirements.txt
```

Minimal `requirements.txt`:
```txt
scikit-learn
tk
pandas
numpy
```

> Note: This script uses custom modules like `imputer`, `scaler`, `encoding`, and `data_sm_transform`. Ensure they are available in your project directory.

---

## 📌 To-Do & Improvements

- [ ] Refactor into modules (UI, logic, file I/O)
- [ ] Improve cross-platform compatibility
- [ ] Turn into CLI package (argparse or Typer)
- [ ] Add error handling & logging
- [ ] Add GUI (Tkinter or PyQt) as optional mode
- [ ] Write unit tests

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](./LICENSE) file for details.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 👨‍💻 Author

Made with 💻 and zero sleep by [Parixit]

> _"2 days of tea-fueled madness and a dream to clean data the right way."_ 😎
