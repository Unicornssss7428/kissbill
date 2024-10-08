<p align='center'>
  <img src=https://github.com/Unicornssss7428/kissbill/blob/main/images/kiss_bill.png title='Kissbill Logo' width='300' height='300'>
</p>
<h2 align='center'>Kissbill</h2>
<p align='center'>Kissbill is a bills tracking/budgeting app written in Python that aims to be as simple to use as possible! All you need to do is tell it when your bills are due and how much they cost you, then it'll do the rest.</p>


# Usage

Create a .toml file that houses all of your bills and paydays with their due dates and amounts.
- Electricty
- Payday1
- Payday2
- PaydayBirthday

The payday keyword is neccesary for a payday as  all other items are treated as bills.
(It doesn't matter what you put after Payday as long as you dont' have two items named exactly the same thing.)

```toml
[Electricity]
due=1
amount=20

[Payday1]
due=1
amount=150

[Payday2]
due=2
amount=140

[PaydayBirthday]
due=14
amount=6000
```


# Why I started this project
I started this project because I grew tired of doing different calculations related to my finances by hand. I didn't want to use a personal finance manager as it seemed a bit overkill for my use case. The original plan for the project was just a small script to calculate
how long it would take for me to save up for an emergency fund then it grew from there. 

A secondary reason that I started this project is because I have a lot of trouble doing math related to my finances and often make impuslive buying decisions. I wanted a way that I could easily see the consequences of my actions without much effort. Hopefully when I get my formal ADHD diagnosis and medications this will be less of an issue. With that being said I hope that this tool helps everybody and if you have ADHD I hope you find some use for it as well :))

# Where this project may go
The overall goal of this project is to be both a useful module for any finance applications you may want to develop and a stand-alone application. 
I don't expect to ever make this into a full-fledged budgeting application that connects with your bank account and helps you manage your finances. At the moment the following features are planned/implemented:

- CLI
- Self-Hosted API so you can query your kissbill while at the store (i.e. POST IP ifispend endpoint). This will be useful for me as I can say "Hey if I buy this new $60000 GPU, how it will affect my goals?"
- GUI
- Ability to calculate how much I can save per day/week/month/year and still pay for expenses.
- Ability to calculate how much money I need to save per day/week/month/year to reach a certain goal, i.e. emergency fund.
- Ability to display a calendar that shows me how much working cash (how much cash I can spend on that day and still meet goals/pay for expenses.) I have each day.
- Ability to calculate how much a certain financial decision affects your ability to save for goals/pay for expenses.
- Ability to calculate total bills for day/week/month/year.
- Ability to calculate total pay for day/week/month/year.
- Eventual port/overhaul to Rust
