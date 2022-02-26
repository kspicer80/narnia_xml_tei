from booknlp.booknlp import BookNLP

model_params={
		"pipeline":"entity,quote,supersense,event,coref",
		"model":"big"
	}

booknlp=BookNLP("en", model_params)
input_file="lww.txt"
output_directory="lwwtestfolder/"
book_id="lww"
booknlp.process(input_file, output_directory, book_id)
