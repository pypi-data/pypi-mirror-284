import sys
import os

from openai import AzureOpenAI

DEFAULT_PROMPT = """
                You are an AI code reviewer. Take the diff provided and analyse it against best coding practices.  

                Generate a small summary of the changes, then highlight any issues in design, style, functionality, complexity, naming, and testing, or any obvious errors. Be specific about any issues you suggest, give line numbers and file names where possible.
                In the last section give your overall opinion rating as a noun or short sentence and an emoji. E.g. "Good to ship! 🚢", "Needs more work 🚧" or "Great work! 🎉"

                Use markdown to format your response with headings and bullet points under the followng headings:

                ### Summary of Changes
                ### Issues
                ### Improvement Suggestions
                ### Opinion Rating 
                
              """


def review_code(diff: str) -> str:
    client = AzureOpenAI(
        azure_endpoint=os.environ.get("AZURE_OPENAI_API_ENDPOINT"),
        api_version=os.environ.get("API_VERSION"),
    )

    completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": DEFAULT_PROMPT,
            },
            {
                "role": "user",
                "content": f"PR TITLE: {os.environ.get('PR_TITLE', 'not provided')}",
            },
            {
                "role": "user",
                "content": f"PR DESCRIPTION: {os.environ.get('PR_BODY', 'not provided')}",
            },
            {"role": "user", "content": diff},
        ],
        model="second-opinion",
    )

    return f"## Second Opinion 🩺 (AI Code Review)\n\n{completion.choices[0].message.content}"

def main():
    if len(sys.argv) < 2:
        print("usage: second-opinion <diff_file>")
        sys.exit(1)

    with open(sys.argv[1], "r") as f:
        diff = f.read()

    opinion = review_code(diff)

    print(opinion)

if __name__ == "__main__":
    main()
