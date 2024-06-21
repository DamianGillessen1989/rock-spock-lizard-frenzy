# The Rock Spock Lizard Frenzy command line based Python game

## Introduction

Welcome to Rock Spock Lizard Frenzy command line Python game! This project marks the third step in my journey towards becoming a proficient Full Stack Developer.

The goal of this project is to create a Rock Spock Lizard Frenzy game which can be played in the command terminal using Python. By combining straightforward gameplay, (hopefully) intuitive design, and a little humour too, I aim to provide users with an entertaining and enjoyable gaming experience.

Developed using a combination of Python and randomisation logic, this project serves as a dynamic application where users can immerse themselves in the thrill of the Rock Paper Scissors Lizard Spock game. From strategic choices to humorous taunts and encouragements, the game offers a range of features to keep players engaged and entertained throughout their gaming sessions.

In this README, I will delve into the project's development process, detailing the planning stages, design considerations, implementation of key features, and the technologies utilised. I hope you find this project both informative and enjoyable as you explore the world of Rock Spock Lizard Frenzy. Thank you for joining me on this exciting adventure!

The live link can be found here - [https://rock-spock-lizard-frenzy-fd1c0328cc20.herokuapp.com/](https://rock-spock-lizard-frenzy-fd1c0328cc20.herokuapp.com/)

## Rock Spock Lizard Frenzy Gaming Experience

I took inspiration from a variety of sources and approaches when developing the Rock Spock Lizard Frenzy game, with the goal of giving users an engaging and entertaining gaming experience. I used ideas from user-centred design and game development methodologies to guide the process.

## Project Development Approach

To create a comprehensive and engaging instructional program, I separated the project's progress into the following stages:

The Discovery stage, Planning stage, Development stage, Testing stage, and Deployment stage.

Each phase was meticulously planned and performed step by step to address various aspects of the program's functioning, content, and user experience. This strategy enabled a user-centric, comprehensive, and iterative development process that prioritised both clear content and user experience.

### Discovery Phase

#### My Goals:

- I intended to streamline the user experience and ensure smooth navigation through the program.
- I tried to improve textual clarity to avoid future user confusion.
- My goal was to evoke favourable emotional responses from users, hence encouraging deeper interaction.
- I worked to ensure that the returned messages was coherent and relevant throughout.
- Finally, I worked on developing the flow so that is made sense, was accessible and did not overwhelm users.

### User Objectives:

  #### Goals for First-time Users:

  - Quickly understand the platform's purpose and scope.
  - Easily navigate through the program.
  - Feel a sense of progress while investigating.
  - Continue browsing easily after any disruptions.

  #### Goals for Returning Visitors:

  - Understand the information that has been offered.
  - Interact with the program/game material without difficulty.
    
### Planning Phase

Taking a systematic approach to my project management, I decided to divide the development process into three separate phases.

#### Phase 1: Conceptualisation

- Plan the logic flow for the Rock Spock Lizard Frenzy game that would be simple to program and easy to understand by users to facilitate enjoyment.
- Plan the skeleton-structure for the Python logic that will be used in the development of the game.

#### Phase 2: Refinement

- Test the game and make any appropriate adjustments necessary for it to function as intended.
- Solicit feedback from peers to gauge usability and functionality.
- Address any identified bugs or issues to enhance user experience.

#### Phase 3: Validation and Finalisation

- Test thoroughly using tools such as the PEP8 Python Validator to confirm compliance with web standards.
- Prepare the project for submission, ensuring that all requirements have been met.

### Development Phase

During the development phase of this project, careful attention was given to creating game-logic that would be engaging and easy-to-understand for all users:

### Blueprint

During the development phase, a detailed logic flow was developed. 

This logic flow is a useful blueprint for understanding the program flow and the user journey. Iterative modifications were made during development to improve the user experience and address usability issues.

![Flow Chart](https://github.com/DamianGillessen1989/rock-spock-lizard-frenzy/blob/main/assets/images/rock-spock-lizard-frenzy-flow-chart.png)!

### Features Present:

- Welcome message - The welcome message and request from user for a set number of rounds to play is presented when the program starts.
![Welcome message](https://github.com/DamianGillessen1989/rock-spock-lizard-frenzy/blob/main/assets/images/welcome-message.png)!
- Players' choice - once the game has started and user has selected a set number of rounds to play, the game then asks the user to make a choice between Rock, Paper, Scissors, Lizard, or Spock.
![Player Choice](https://github.com/DamianGillessen1989/rock-spock-lizard-frenzy/blob/main/assets/images/player-choice.png)
- Game flow - The game then follows the usual Rock Paper Scissors Lizard Spock rules and presents the player with a fun string of informational replies. The player is then requested for their next choice, if necessary. Player and computer scores are presented.
![Game Process](https://github.com/DamianGillessen1989/rock-spock-lizard-frenzy/blob/main/assets/images/game-process.png)
- Final Scores - Once the set number of rounds is completed the 'final score' is presented to the user and they are then asked if they want to play again.
![Final Scores](https://github.com/DamianGillessen1989/rock-spock-lizard-frenzy/blob/main/assets/images/final-scores.png)
- Goodbye message - Once the user selects 'no' and decides to discontinue the program, they then are presented with a goodbye message and a link to my other projects.
![Goodbye Message](https://github.com/DamianGillessen1989/rock-spock-lizard-frenzy/blob/main/assets/images/goodbye-message.png)

### Features to Implement:

- In the future I might be open to installing some graphics for the game or some ASCII art representing each of the 5 potential choices or developing a GUI.
- Adding the technology for multi-player facility would be fun also, so player can choose whether to play vs another player or vs the computer.
- I could potentially implement game statistics and leaderboards in order to provide players with a sense of progression and achievement.

## Technologies Used:

### Development Tools and Frameworks:

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - this program was developed fully using Python3.

### Styling and Design Elements:

- [CI Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template) - Provides all the necessary files for the program to be presented nicely in Heroku.

### Development and Testing Utilities:

- [GitHub](https://github.com/) - Repository in which project code is stored after pushes and commits.
- [Git](https://git-scm.com/) - Supervises version control and permits commits and pushes using the Gitpod terminal.
- [Visual Studio Code](https://code.visualstudio.com/) - This was the principal environment for code development.

### Optimisation and Quality Assurance:

- [Grammarly](https://app.grammarly.com/) - Used to check content throughout the production process.
- [PEP8 Python Validator](https://pep8ci.herokuapp.com/) - Used to validatea the Python code of the program and ensure deployability on Heroku.
- [Heroku](https://www.heroku.com/) - Used to deploy the program.

## Testing Phase

As much of the programs elements were provided in the CI template for this project the amount of testing required for this project was fairly straight-forward or basic. I still attempted to conduct a thorough testing approach to ensure the game's optimal operation and efficiency. The following efforts were taken to ensure the program's integrity and user experience:

### Testing and Evaluation

1. Cross-Platform Compatibility: The game was thoroughly tested across various operating systems, including Windows, macOS, and Linux, to ensure consistent performance and functionality.

2. User Input Validation: Extensive testing was conducted to ensure the game accurately captures and processes user inputs. Special attention was given to verifying correct functionality when users input valid choices and handling invalid inputs gracefully.

3. Randomness and Fairness: The randomness of the computer's choices was rigorously tested to ensure fairness. Multiple iterations of gameplay were simulated to confirm that the distribution of choices (Rock, Spock, Paper, Lizard, Scissors) was even and unbiased.

4. Functionality Testing: All game mechanics, such as the comparison of choices, score tracking, and end-of-game conditions, were thoroughly tested to ensure they operate correctly and provide accurate results.

5. Feedback Messages: Detailed feedback messages were reviewed to ensure they correctly reflect the outcome of each round, providing clear and accurate information to the player about why a particular choice won or lost.

6. Edge Case Handling: Various edge cases were tested, such as extremely high numbers of rounds, rapid input entries, and unusual input sequences, to ensure the game handles these scenarios without errors or crashes.

These testing techniques enabled the identification and correction of any issues or inconsistencies, resulting in a reliable and enjoyable game experience.

### Future Testing
I hope to be able to add the following testing processes to "Rock Spock Lizard Frenzy" in the future:

1. Performance Testing:

    - Load Times: Measure the execution time of various functions, especially those that involve user input and random choice generation, to ensure the game runs smoothly.
    - Resource Usage: Monitor CPU and memory usage to ensure the game is efficient and does not cause unnecessary strain on the system.

2. Usability Testing:

    - User Experience: Conduct user testing sessions to gather feedback on the game's ease of use and overall enjoyment.
    - Error Handling: Ensure the game provides helpful error messages and guides users to correct invalid inputs without frustration.

3. Compatibility Testing:

    - Cross-Platform Testing: Test the game on different operating systems (Windows, macOS, Linux) to ensure consistent behavior and performance.
    - Python Versions: Verify compatibility with multiple Python versions to ensure broad accessibility.

4. Accessibility Testing:

    - Screen Readers: Ensure the game can be used with screen readers for visually impaired players.
    - Keyboard Navigation: Confirm that all game functions can be accessed and controlled using only the keyboard.

5. Security Testing:

    - Input Validation: Ensure all user inputs are properly validated and sanitized to prevent injection attacks or other malicious exploits.
    - Data Integrity: Test that scores and game state data are accurately maintained and cannot be easily tampered with.


6. Stress Testing:

    - High Input Volume: Simulate scenarios where a large number of inputs are processed in quick succession to ensure the game remains stable and responsive.
    - Extended Play: Run the game for extended periods to identify any memory leaks or performance degradation over time.

7. Regression Testing:

    - Feature Testing: Re-test all features after any updates or changes to ensure no existing functionality is broken.
    - Bug Fixes: Verify that previously identified bugs remain fixed in future versions.

8. Automated Testing:

    - Unit Tests: Develop a comprehensive suite of unit tests for all game functions to catch errors early in the development process.
    - Integration Tests: Ensure all components of the game work together seamlessly by creating automated integration tests.

Implementing these future testing processes will help maintain the quality, reliability, and accessibility of "Rock Spock Lizard Frenzy," ensuring a positive experience for all players.

### Validator Testing

I conducted testing using the PEP8 Python Validator to ensure the validity and adherence to Heroku deployment standards.

1. PEP8 Python Validator: The Python code was validated using the PEP8 Python Validator, which looked for missing components, syntactical errors, and Python standard conformance.
- PEP8 Python Validator Test Results
![PEP8 Python Validator test results](https://github.com/DamianGillessen1989/rock-spock-lizard-frenzy/blob/main/assets/images/pep8-validator.png)

2. ExtendsClass Python syntax checker: I also used the ExtendsClass Python syntax checker to ensure the python code was correct and compliant with Python standards.
- ExtendsClass Python syntax checker Test Results
![ExtendsClass Python syntax checker test results](https://github.com/DamianGillessen1989/rock-spock-lizard-frenzy/blob/main/assets/images/extends-class.png)

After completing this rigorous validator testing, I was able to identify and correct any coding errors, accessibility concerns, or performance issues, hopefully resulting in a compliant, user-friendly, and high-performing website.

## Resolved and Unsolved Bugs

### Resolved Bugs

Several issues were identified and rectified during the Rock Spock Lizard Frenzy program construction process with hopes to optimise operation and improve user experience.

- Initially, when the program was run, the user was getting duplicate win/loss notifications. To fix this issue, I located and removed the duplicate code that was responsible for the unneccessary win/loss message. [Dup win/loss bug image](https://github.com/DamianGillessen1989/rock-spock-lizard-frenzy/blob/main/assets/images/duplicate-win-notification-bug.png) - [Dup win/loss bug image two](https://github.com/DamianGillessen1989/rock-spock-lizard-frenzy/blob/main/assets/images/duplicate-win-notification-bug-two.png)

- An issue arose with the 'best of x rounds' function - if a user entered the wrong format of reply in the terminal, in this case an integer, the program crashed and the user saw a convaluted error message. To fix it I added the feature indicating to the player their reply needs to be an integer. This took a couple of attempts to fix, see the two error messages here: [Best of rounds bug image one](https://github.com/DamianGillessen1989/rock-spock-lizard-frenzy/blob/main/assets/images/best-of-rounds-bug.png) - [Best of rounds bug image two](https://github.com/DamianGillessen1989/rock-spock-lizard-frenzy/blob/main/assets/images/best-of-rounds-two-bug.png)

### Unresolved Bugs

- There are no remaining bugs in the code that I can find - the program seems robust enough to take most forms of potential input and guide the user through wherever they go wrong. At this time, as it's such a simple game, I think there is little room for error. Any potential changes are more design or ux-related choices that can improve the overal program and experience.

## Deployment Phase

Upon completing the development phase of Rock Spock Lizard Frenzy, the focus shifted to deploying the site for online accessibility. The deployment strategy was meticulously crafted, harnessing the synergy of Visual Studio Code (VSC), Sourcetree, and Git/GitHub to seamlessly transition from development to production.

#### 1. Version Control with Git/GitHub:

- Git served as the backbone of the version control system throughout the development journey.
- Every code tweak and enhancement was meticulously logged using Git, fostering efficient collaboration and enabling swift rollbacks to prior versions if required.
- GitHub acted as the secure cloud-based repository housing the project's codebase.
- Regular commits were executed to maintain a detailed history of the project's evolution and changes.

#### 2. Cloning or Forking a Repository in GitHub:

- To clone or fork a GitHub repository, start by navigating to the repository page on GitHub. If you want to clone the repository, locate the green "Code" button and click it. You'll see options to clone using HTTPS, SSH, or GitHub CLI.
- Copy the URL provided for your preferred method. Open your terminal or Git Bash and run the command git clone <URL>, replacing <URL> with the copied URL. This will create a local copy of the repository on your machine.
- If you prefer to fork the repository, click the "Fork" button at the top right corner of the repository page. This will create a personal copy of the repository under your GitHub account.
-You can then clone this forked repository to your local machine using the same git clone command.

#### 3. Development Environment with Visual Studio Code (VSC):

- Visual Studio Code (VSC) emerged as the go-to integrated development environment (IDE) for crafting and refining the website's code.
- VSC's user-friendly interface and robust toolset streamlined coding, debugging, and testing processes.
- Productivity was further amplified by leveraging extensions like Live Server and GitLens, providing invaluable insights into the development workflow.

#### 4. Deployment Process with Sourcetree:

- Sourcetree, a feature-rich Git GUI client, played a pivotal role in simplifying the deployment workflow and visual management of the Git repository.
- Advanced functionalities such as branching and merging facilitated parallel development and seamless integration of new features.
- The deployment workflow entailed pushing the finalized codebase from the local repository to the remote repository on GitHub via Sourcetree.

#### 5. Hosting on Heroku:

- The Heroku local Python environment was selected as the ideal platform for hosting the "Rock Spock Lizard Frenzy" command line game.
- Execution of the game was seamlessly initiated from the Heroku local Python environment, leveraging built-in functionality to run Python scripts, via Github.
- Continuous testing and updates were configured to automatically execute and validate changes to the game upon making modifications to the main script.

#### 6. Final Testing and Verification:

- Rigorous testing was conducted to validate the game's functionality and compatibility across different operating systems and Python versions before release.
- Thorough debugging, performance assessments, and user experience evaluations were carried out to deliver an engaging and reliable gaming experience.
- Any identified issues were promptly addressed, and necessary refinements were implemented to ensure the game met the highest standards of quality and user satisfaction.

In conclusion, the deployment of the "Rock Spock Lizard Frenzy" game was executed meticulously to guarantee a smooth and successful transition from development to distribution. The careful planning and testing processes employed throughout the deployment lifecycle ensured that the game was delivered with precision and professionalism, ready to provide an enjoyable and challenging experience for players everywhere.

- The site was deployed to Heroku. The steps to deploy are as follows: 
  - In the Heroku dashboard, navigate to the Settings tab and apply the appropriate settings there.
  - From the deploy section, connect the correct GitHub repository, and hit 'manually deploy' at the bottom of the page.
  - The program will be automatically deployed at which point you can access the app and run the program. 

The live link can be found here - [https://rock-spock-lizard-frenzy-fd1c0328cc20.herokuapp.com/](https://rock-spock-lizard-frenzy-fd1c0328cc20.herokuapp.com/)

## Credits

### Development Tools and Frameworks

- [**Python**](https://en.wikipedia.org/wiki/Python_(programming_language)) - this program was developed fully using Python3.

### Development and Testing Utilities

- [**GitHub**](https://github.com/) - Repository for storing project code after commits and pushes.
- [**Git**](https://git-scm.com/) - Manages version control, with Gitpod terminal facilitating commits and pushes.
- [**Visual Studio Code**](https://code.visualstudio.com/) - Served as the primary development environment.
- [**Anandvikas**](https://gist.github.com/EricPPeterson/77c4c92c63757cb4426c) - Inspiration for the game mechanics for the Rock Paper Scissors Lizard Spock game.

### Optimization and Quality Assurance

- [**Grammarly**](https://app.grammarly.com/) - Employed to rectify grammar errors across the project, ensuring polished content.
- [**PEP8 Python Validator**](https://pep8ci.herokuapp.com/) - Used to validatea the Python code of the program and ensure deployability on Heroku.
- [**Heroku**](https://www.heroku.com/) - Used to deploy the program.

### Acknowledgements

I would like to thank the following individuals and sources for their significant assistance and support while this project was being developed:

- My Code Institute peers and instructors, who provided useful comments and guidance throughout the creation and testing phases. Special thanks to Thomas for his constant input and assistance.
- To my daughter Thea, who is the love of my life.

I am grateful to everyone who contributed to the project's success, either directly or indirectly. Your encouragement and support have been important in helping me reach my aim with this website.