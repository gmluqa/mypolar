# mypolar

A self-hosted bipolar mood tracking diary.

# What is it?

Mypolar was a tool I designed for my own personal usage to track my bipolar mood cycles and display the data visually.

# How it works

You run the app.py daily, and the app.py will prompt you to input how you're feeling today (scale of 1 - 10, 1 being suicidally depressed and 10 being full blown manic), it will ask you how many pills you're gonna take today and then will ask which ones (you input a pill type by selecting it from the CLI, the options are: "Depakine Chrono 500mg", "Pristiq 50mg"), once you select one, it prompts you for how many you will take/have taken today of that specific pill.

After all of this, the app will write to a file called data.json located in the path local/data.json with the following kind of struture:

```
    {
  "01/01/2001": [
    {
      "pill": "Depakine Chrono 500mg",
      "quantity": 1
    },
    {
      "pill": "Pristiq 50mg",
      "quantity": 1
    }
  ],
  "02/01/2001": [
    {
      "pill": "Depakine Chrono 500mg",
      "quantity": 1
    },
    {
      "pill": "Pristiq 50mg",
      "quantity": 1
    }
  ]
}
```

# Instructions

I made this for personal usage, so it only lists pills I personally take, if you would like more listed, let me know or submit a PR.
