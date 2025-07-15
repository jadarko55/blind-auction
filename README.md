# Blind Auction

A simple command-line blind auction program written in Python where multiple bidders can participate in a secret auction.

## Description

This program simulates a blind auction where:
- Multiple participants can enter their names and bid amounts
- Each bidder's information is kept secret from other bidders
- The program determines the winner with the highest bid
- The screen is cleared between each bidder for privacy

## Features

- ASCII art logo display
- Multiple bidder support
- Screen clearing for bid privacy
- Automatic winner determination
- Input validation for bid amounts

## Installation

1. Clone this repository:
```bash
git clone https://github.com/jadarko55/blind-auction.git
cd blind-auction
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the program:
```bash
python main.py
```

Follow the prompts:
1. Enter your name
2. Enter your bid amount (numbers only)
3. Indicate if there are more bidders (yes/no)
4. Repeat for each additional bidder
5. The program will announce the winner

## Files

- `main.py` - Main program logic and user interface
- `art.py` - Contains the ASCII art logo
- `requirements.txt` - Python dependencies

## Requirements

- Python 3.x
- replit package (for screen clearing functionality)

## Example Run

```
[ASCII Art Logo]
What is your name? Alice
How much will you bid.
$150
are there any more bidders. yes or no.
yes

[Screen clears]
What is your name? Bob
How much will you bid.
$200
are there any more bidders. yes or no.
no

The winner of the auction was Bob with a bid of 200
```

## Contributing

Feel free to fork this project and submit pull requests for any improvements.
