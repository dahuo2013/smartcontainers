Feature: Linked Data Platform

    Scenario: LDP creates LDP container
        Given a HTTP POST command
        When it is given to LDP to create a container
        Then it should create a file folder at end point
        And it create a meta file with provenance information

    Scenario: LDP creats LDP resourse
        Given a HTTP POST command
        When it is given to LDP to create a resource
        Then it should create a binary file at end point
        And it create a meta file with provenance information
        And it update meta file of the container

    Scenario: LDP gets LDP container information 
        Given a HTTP GET command
        When it is given to LDP to create a container
        Then it should create a file folder at end point
        And it create a meta file with provenance information

    Scenario: Smart containers intercept the build command and store information in the containers label
        Given a docker build command
        When it is given to smart containers to run
        Then it should extract the command line information
        And it should excecute successfully
        And it adds a label to the executed container

    Scenario: Smart containers intercept the commit command and store information in the containers label
        Given a docker commit command
        When it is given to smart containers to run
        Then it should extract the command line information
        And it should excecute successfully
        And it adds a label to the executed container

