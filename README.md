Author: Jared Manusig
Email: jmanus2@uic.edu

1. This program is used to preprocess a collection and do a simple statistical analysis on the preprocessed data. Program explores the word count, vocabulary size, top 20 words, and minimum number of words to account of 15% of the total number of words in the collection. Furthermore, the program implements the Porter Stemmer algorithm from the nltk library and removes stopwords based on the nltk library of stop words. After cleaning the data, the program outputs the same statistical analyis from above. 

2. How to run: 
    Given that the citeseet directory is in the same directory as the py file, 
    Using python3, use the command "python3 582a1.py" to run the program

    If a directory other than citeseer is used, change line 119 to the desired file or directory and add the directory or file to the working directory. Run the program with the command above.

3. Answers 

    2a. Total number of words: 488662

    2b. Vocabulary Size:  17321

    2c. Top 20 Words: 
        1. the 25724,
        2. of 18713,
        3. and 14199,
        4. a 13418,
        5. to 11644,
        6. in 10104,
        7. for 7383,
        8. is 6579,
        9. we 5150,
        10. that 4821,
        11. this 4448,
        12. on 3783,
        13. are 3739,
        14. an 3284,
        15. with 3200,
        16. as 3078,
        17. by 2789,
        18. data 2763,
        19. based 2534,
        20. be 2505

    2d. The stop words from this list are: 
        1.  the,
        2.  of,
        3.  and,
        4.  a,
        5.  to,
        6.  in,
        13. are 3739
        7.  for,
        8.  is,
        9.  we,
        10. that,
        11. this,
        12. on,
        13. are,
        14. an,
        15. with,
        16. as,
        17. by,
        13. are 3739
        18. be,

    2e. Minimum number of words to account for 15 percent of total words:  5


    3a.Total number of words:  304288

    3b. Vocabulary Size:  11334

    3c. Top 20 Words: 
        1. system 3766
        2. use 3748
        3. agent 3258
        4. base 2763
        5. data 2763
        6. inform 2437
        7. model 2349
        8. paper 2249
        9. queri 1944
        10. user 1884
        11. learn 1820
        12. 1 1783
        13. algorithm 1597
        14. problem 1575
        15. web 1560
        16. comput 1554
        17. applic 1551
        18. approach 1546
        19. present 1508
        20. databas 1442

    3d. None because stopwords were removed 

    3e. Minimum number of words to account for 15 percent of total words:  23
