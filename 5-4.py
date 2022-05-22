

letter = """

Dear {salutation}{name}

Thank you for your letter. we are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}

Send us your receipt and {amount} for shipping and Handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}

Thank you for your support.

Sincerely,
{spokesman}
{jobtitle}""".format(salutation = "Sr.", name = "David", product = "tea", verbed = "transfered", room = "garage", animals = "rat",
amount = "six", percent = "60", spokesman = "Lisa", jobtitle = "AAA Ltd")

print(letter)
