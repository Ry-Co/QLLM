# main.py
import asyncio
import api_handler
from api_handler import chat

def main():
    print("Chat with the bot! Type 'quit' or 'exit' to stop.")
    asyncio.run(chat())

main()

# api_handler.py


# lets test the effcicacy of instruction vs structured output with the reddit comment questions idea./
# what do we need?
#--------------------------------------------------------#
# LLM interface where I can pass prompts + the standard wrapper query with the required format
# Something to get random prompts to test the LLMs consistency. ( Reddit scraper for random questions)
# I want to test whether an LLM can keep itself from responding outside the designated format even when the queries are completely unrelated to its "meta-query" task.
# if they can't, then I think it really calls into question what the context vector is even doing. It's a major bottleneck so I think more intuition around this is valuable regardless of the outcome.



# I think scraping random questions from the internet will be a good way of generating coherent, human-esque, queries.
# Also, there is functionality in most LLM libraries to force the LLM to return in a certain schematic. PyDantic is the broad solution here.
# I think this is nonsense. Effectively what we're doing is layering another layer of interpretation ontop of interpretation to try and get a consistent format. 
# my question would be, why bother with the LLM's interpretative abiltiies if we can't even trust it to follow a basic formatting strcuture. I get using this if the format isn't the main focus of whatever the functionality within the app is fulfilled by the LLM
# but for the usecase outline in this app- as well as other non-public projects- This fix makes me ask why I would not just point the pydantic or some other interpretor and a series of fuzzy matches at the user input.
# the LLMs should be able to perform consistently in terms of format - even if the query input is utterly random so long as the query doesn't blow out the context window(at least I think)








