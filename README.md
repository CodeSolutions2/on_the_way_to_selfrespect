# on_the_way_to_selfrespect

A JavaScript memorization game productivity tool to help users learn about self-respect and/or self-esteem. Unorganized activities that many people call 'fun' (like hanging out, chatroom, video games, etc..) do not always promise that participants will learn important life lessons like self-esteem and self-respect. Constantly engaging in unorganized activities without learning self-respect can create a vicious cycle where individuals do not know what self-respect is, nor understand how to treat themselves with respect and others with respect.

Self-respect is knowing that one can always "do better", learn, and achieve the necessary things in life to live in society responsibily and happily. 

Dictionary citations: 
  - Dictionary.com : "proper esteem or regard for the dignity of one's character."
  
When one thinks that they can not "do better", they think that they are a victim. Many "victim belivers" think that they deserve or it is allowable to use/hurt others that are "doing better in life" in order for them to "survive" (ie: acheive better life success). "Victim belivers" (ie: people with low self-respect/esteem) do not have confidence/belief in their ownselves, which is the definition of self-respect (to have belief and confidence in one's self), such that they can do better or acheive success all by themselves. 

Thus, "Victim belivers"/low self-respect/esteem people disrespect themselves and they disrespect others. Please learn about self-respect such that everyone can suceed in life together, and the world can be a less violent place.

This memorization game was made to help people to start to think about self-respect.

[Completed working version] https://CodeSolutions2.github.io/on_the_way_to_selfrespect/index11.html

## Construction of JavaScript video game
  - View an explanation of this webapp on my Medium Practicing DatScy blog: https://medium.com/@j622amilah/javascript-tensorflow-js-webapp-game-d17aa84422f0
  - This video game contains two (3-dense layer) neural network categorical models to predict: [0] flash number (how many squares should flash at each round), and [1] presentation time interval (how long each square should flash). These variables are randomly choosen for the first round, and then for the following rounds the model uses your previous round performance to predict the next variable. In the beginning, without a lot of data, it will randomly predict flash number/presentation time interval. However, as the game progresses it will find associations of flash number/presentation time interval with how fast and accurately you responded. For example, if you responsed slow and inaccurate for 10 rounds and the last round, it will predict flash number/presentation time intervals where you previously responded slow and inaccurate, thus giving you a chance to change or maintain how you previously behaved.
    - The following performance parameters are stored each round for model prediction: [round accuracy, total accuracy, round response time, presentation time interval, flash number
    - At the end of each round, a "wisdom" message about how to have better self-respect is presented

      

## Upwork

[Available for purchase on Upwork](https://www.upwork.com/services/product/development-it-tensorflow-js-performance-prediction-javascript-video-game-development-1767599520868958208)
