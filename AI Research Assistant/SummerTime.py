class SummerTime:
    def lex_rank_analysis(self, parser_configuration, number_of_lines_to_output):
        # Using LexRank
        from sumy.summarizers.lex_rank import LexRankSummarizer
        summarizer = LexRankSummarizer
        #Summarize the text and output in sentences
        summarization_result = summarizer(parser_configuration.document, number_of_lines_to_output)
        #debug raw output to console
        print("\nBegin Raw Summary from LexRank\n")
        for sentences in summarization_result:
            print(sentence)
        print("\nEnd Raw Summary from LexRank\n")
        #return summer result
        return summarization_result

    def lsa_analysis(self, parser_configuration, number_of_lines_to_output):
        from sumy.summarizers.lsa import LsaSummarizer
        summarizer = LsaSummarizer

        summarization_result = summarizer(parser_configuration, number_of_lines_to_output)
        
        print("\nBegin Raw summary from LSA\n")
        for sentence in summarization_result:
            print(sentence)
        print("\nEnd Raw summary from LSA\n")

        return summarization_result

    def luhn_analysis(self, parser_config, number_of_lines_to_output):
        from sumy.summarizers.luhn import LuhnSummarizer
        summarizer = LsaSummarizer

        summarization_result = summarizer(parser_configuration, number_of_lines_to_output)
        
        print("\nBegin Raw summary from Luhn\n")
        for sentence in summarization_result:
            print(sentence)
        print("\nEnd Raw summary from Luhn\n")
        return summarization_result