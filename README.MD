# FinvinciCurrencyConverter

This is a small REST application to convert any amount of money from one currency to another at the latest rates using the **/convert** API endpoint. Available currencies: **USD, EUR, CZK, PLN**.

**Definition**

https://<span></span>finvinci-currency-converter.herokuapp.com/api/convert?amount={amount}&from={from}&to={to}

**Parameters**

- **amount** (float)<br>
The amount to be converted

- **from** (string)<br>
The base ('from') currency (3-letter code)

- **to** (string)<br>
The target ('to') currency (3-letter code)

All parameters are required.

**Example**

https://finvinci-currency-converter.herokuapp.com/api/convert?amount=100&from=CZK&to=EUR

**Result Format**

```json
{
  "response": 4.002276
}
```

The converted amount is given in the response parameter.