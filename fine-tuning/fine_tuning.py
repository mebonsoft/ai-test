import openai

openai.api_key = "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"
openai.File.create(
  file=open("example.jsonl", "rb"),
  purpose='fine-tune'
)

createid="file-Bfrsk83VhoFIUDS2kNdOrOye"
jobid = "ftjob-oVqytOeWEEhHdwgsMZcSRycW"