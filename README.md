# DeduplicateData

For this challenge I used Python, Pandas Modules, because I think.

I started by reading the data and drop a few columns:
 - page_url, not useful 
 - manufacturing_year, all the values were -1

I removed any leading/trailing whitespace from the product_title column so I can sort it properly after. 
I goruped the rows by product_title so I can have all the duplicates in one and applied the function above.

# The Function:
- I choosed to keep the longest description of the product and keep the index of the row to help me choose for the 'price' column. I observed that in some descriptions the price is also found and sometimes has different currency, so I wanted to match the descriptions.
- For the other columns, I have almost the same logic, the cell with the most information will be kept and if neither one has it, than will be replace with "Information not found". 
