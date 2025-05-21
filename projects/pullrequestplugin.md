# Bitbucket Server Repository Pull Request Hook Plugin

*This project, including source code is discontinued. It is simply not relevant to the up to date versions of Bitbucket*

![alt](/projects/bitbucket/repopullrequest-pluginlogo.png)

* [Atlassian Marketplace](https://marketplace.atlassian.com/plugins/com.maciejkucia.atlasbbplugin.repopullrequest/server/overview)
* [Sources](https://github.com/MaciejKucia/bitbucket-server-repopullrequest)

## Planned features

  * Multiple URLs
  * Support for HTTPS
  * Internationalization

## Introduction

The plugin provides the following functionality:
  * Notifying 3rd party services via REST interface about the changes in the project Pull Requests
  * Notification on:
    * PR creation/edit
    * PR decline
    * PR merge
    * New/Edit/Delete comment in the PR
  * Per-repository configuration via 'repository hooks' tab
  * Accessible by the repository administrators
  * The following HTTP operations are supported:
    * POST
    * GET
    * PUT
    * DELETE

## Usage

### Templating

Several variables can be passed by the message URL or body. There is a special variable containing
comma separated list of available variables: 
`${all_keys}`

![alt](/projects/bitbucket/bb_body_json.png)

### Authorization

There is no dedicated field for authorization. One can add authorization header into 'headers'. 
In such case the field will look like:

![alt](/projects/bitbucket/bb_auth_headers.png)

Please visit [wikipedia](https://en.wikipedia.org/wiki/Basic_access_authentication) to learn how to construct basic auth header.

For Jenkins it is recommended to use 
[Build Token Root Plugin](https://wiki.jenkins-ci.org/display/JENKINS/Build+Token+Root+Plugin).
It allows using anonymous request + build token (think of API key).

## Example 1 ##
  - Create Jenkins job "Bitbucket Capture"
    - Add String Parameter `ALL`
    - Add Token `BBBUILD` in `Build Triggers` `Trigger builds remotely (e.g., from scripts)`
  - Check if the job is working
    - Trigger job manually using your browser's private mode
    - Enter the (appropriate to your setup) URL `http://localhost:8080/buildByToken/buildWithParameters?token=BBBUILD&job=Bitbucket%20Capture&ALL=Hello`

Entering URL will take you to an empty page. Back in Jenkins you should see that the job was triggered and parameter is successfully passed:

  - Add more String Parameters to the Jenkins job:
    - `ACTION`
    - `PR_ID`
    - `REPO`
    - `PROJECT`
  - Configure Bitbucket Server
    - Ensure that the plugin is installed.
    - Enter any repository Settings, then Hooks
    - Enable `Pull Request Hook`
    - Enter URL `http://localhost:8080/buildByToken/buildWithParameters?token=BBBUILD&job=Bitbucket%20Capture&ALL=${all_keys}&ACTION=${action}&PR_ID=${pr_id}&REPO=${repo}&PROJECT=${project}`
    - Enable all triggers
    - Save

![alt](/projects/bitbucket/bb_example1_1.png)
![alt](/projects/bitbucket/bb_example1_3.png)
![alt](/projects/bitbucket/bb_example1_5.png)

  - Test connection
    - Create pull request
    - Add a comment

After that you should notice that a new builds were run. Inspect those builds parameters.

![alt](/projects/bitbucket/bb_example1_2.png)

#### Extras

Jenkins job `config.xml`:

```
<project>
  <actions/>
  <description/>
  <keepDependencies>false</keepDependencies>
  <properties>
    <hudson.model.ParametersDefinitionProperty>
      <parameterDefinitions>
        <hudson.model.StringParameterDefinition>
          <name>ALL</name>
          <description/>
          <defaultValue/>
        </hudson.model.StringParameterDefinition>
      </parameterDefinitions>
    </hudson.model.ParametersDefinitionProperty>
  </properties>
  <scm class="hudson.scm.NullSCM"/>
  <canRoam>true</canRoam>
  <disabled>false</disabled>
  <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
  <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
  <authToken>BBBUILD</authToken>
  <triggers/>
  <concurrentBuild>false</concurrentBuild>
  <builders/>
  <publishers/>
  <buildWrappers/>
</project>
```

## Displaying Log

There is a button in the configuration dialog that leads to a log. Communications are logged per-repository.
<<:projects:bitbucket:bb_example_viewlogs.png?nolink|>>

![alt](/projects/bitbucket/bb_example_viewlogs.png)

## Notes

  * Connection time-out is set to 5 seconds

## Test scenarios

### Configuration

  * Entering incorrect URL
    * `https:\\123.com`
    * `45434.com`
    * `http:\\ space .com`
  * Entering incorrect header data
    * without colon
    * empty lines

### Core
  * Enable all notification types and check them one-by one
  * Set all possible variables in body and check if it is valid for all notification types
  * Use basic-auth header

### Weblog
  * Accessing non-existing log
  * Accessing existing log by admin of other project
  * Accessing log with non-configured plugin for given repository
  * Accessing log when non-existing URL is set in config
