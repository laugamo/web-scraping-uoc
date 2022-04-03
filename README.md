# web-scraping-uoc

<!-- PROJECT LOGO -->
  <p align="left">
    Application to get job offers information.
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

This project aims to create an application to get information about job offers.
Its development is in its early stages.
The idea of making a bot that collects the information of the different offers, arises from the need to avoid looking for this information manually and thus save time for the user. Within Linkedin, in order to create an API that collects this information, you need a Linkedin developer account. For this reason, a Python code is implemented to do this for free.
It is proposed to search for job vacancies using a keyword and a location. It is interesting to gather information that allows you to filter the most interesting offers for the user. For example, you can get information such as how long these offers take on Linkedin, the type of schedule they ask for, the experience needed to get the job done, and so on.
<p align="right">(<a href="#top">back to top</a>)</p>


### Built With

* [Spyder.js](https://docs.spyder-ide.org/5/installation.html)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started
To run the application please follow the next steps.

### Prerequisites

1) In order to use this aplicatin you must have a user and password in LinkedIn.
   Both will be required as parameters at the beginning of the main script (main.py)


### Installation

1. Download Spyder [Spyder.js](https://docs.spyder-ide.org/5/installation.html)

2. The application is using the following packages. Please install them before running.
  ```
    selenium
    time
    pandas
  ```

<!-- USAGE EXAMPLES -->
## Usage
You can run this application opening Spyder and pressing the Run button to run the main.py script.
You need to specify the use and the password in order to log in in LinkedIn.
You can also specify the amount of pages you want to fetch the information offers from.


<!-- ROADMAP -->
## Roadmap

- Update config 
- Clean data so that it can be further processed in Power BI or other visualization tools.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Oriol Toll   - otoll@gmail.com
Laura Gassó  - lgm@gmail.com

<p align="right">(<a href="#top">back to top</a>)</p>


