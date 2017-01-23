<div class="ureact-markdown--markdown--3IhZa ureact-markdown"><h1 id="getting-started">Getting Started</h1>
<p>In the course <a href="https://www.udacity.com/course/viewer#!/c-ud171/l-7622549548/m-48403788" target="_blank">“Intro to Backend,”</a> we walk you through the development of a blog application using Google App Engine. But the course excludes certain features that you’ll need to implement for this project.</p>
<p>This document is intended to guide you through implementing the entire project, including what has been taught in the course. Note that some details are omitted from this document, so refer to the <a href="https://review.udacity.com/#!/projects/7508498640/rubric" target="_blank">rubric</a> for details. If you’ve already completed the project from the course, go to step 5.</p>
<p><strong>Note:</strong> Google App Engine has changed a lot recently! Fortunately their documentation is very good. If you encounter error messages while deploying your project, check out <a href="https://cloud.google.com/appengine/docs/" target="_blank">the documentation</a> or ask on the Udacity discussion forums!</p>
<h1 id="let-s-get-started">Let’s Get Started</h1>
<h2 id="setup">Setup</h2>
<ul>
<li><a href="https://www.python.org/downloads/" target="_blank">Install Python</a> if necessary.</li>
<li><a href="https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python" target="_blank">Install Google App Engine SDK</a>.</li>
<li><a href="https://console.cloud.google.com/appengine/" target="_blank">Sign Up for a Google App Engine Account</a>.</li>
<li>Create a new project in <a href="https://console.cloud.google.com/" target="_blank">Google’s Developer Console</a> using a unique name.</li>
<li>Follow the <a href="https://cloud.google.com/appengine/docs/python/quickstart" target="_blank">App Engine Quickstart</a> to get a sample app up and running.</li>
<li>Deploy your project with <code>gcloud app deploy</code>.<ul>
<li>View your project at unique-name.appspot.com.</li>
<li>You should see “Hello World!”</li>
</ul>
</li>
<li>When developing locally, you can use <code>dev_appserver.py</code> to run a copy of your app on your own computer, and access it at <a href="http://localhost:8080/" target="_blank">http://localhost:8080/</a>.</li>
<li>Install Jinja and create helper functions for using Jinja, <a href="https://www.udacity.com/course/viewer#!/c-ud171/l-7557055667/m-686598825" target="_blank">follow the directions here</a>. <ul>
<li>If you’re unfamiliar with Jinja <a href="https://classroom.udacity.com/nanodegrees/nd004/parts/0041345403/modules/750849864075460/lessons/7557055667/concepts/6625293520923#" target="_blank">watch Lesson 2</a> and/or <a href="http://jinja.pocoo.org/docs/dev/" target="_blank">check out the docs</a>.</li>
</ul>
</li>
</ul>
<h2 id="step-1-create-a-basic-blog">Step 1: Create a Basic Blog</h2>
<ul>
<li>Blog must include the following features:<ul>
<li>Front page that lists blog posts.</li>
<li>A form to submit new entries.</li>
<li>Blog posts have their own page.</li>
</ul>
</li>
<li><a href="https://classroom.udacity.com/nanodegrees/nd004/parts/0041345403/modules/750849864075460/lessons/7622549570/concepts/485084250923#" target="_blank">View instructions and solutions here</a>.</li>
</ul>
<h2 id="step-2-add-user-registration">Step 2: Add User Registration</h2>
<ul>
<li>Have a registration form that validates user input, and displays the error(s) when necessary.</li>
<li>After a successful registration, a user is directed to a welcome page with a greeting, “Welcome, <em>[User]</em>” where <em>[User]</em> is a name set in a cookie.<ul>
<li>If a user attempts to visit the welcome page without being signed in (without having a cookie), then redirect to the Signup page.</li>
</ul>
</li>
<li>Watch the <a href="https://classroom.udacity.com/nanodegrees/nd004/parts/0041345403/modules/750849864075460/lessons/7600631235/concepts/486660700923#" target="_blank">demo</a> for more details.</li>
<li>Be sure to store passwords securely.</li>
</ul>
<h2 id="step-3-add-login">Step 3: Add Login</h2>
<ul>
<li>Have a login form that validates user input, and displays the error(s) when necessary.</li>
<li>After a successful login, the user is directed to the same welcome page from Step 2.</li>
<li>Watch the <a href="https://classroom.udacity.com/nanodegrees/nd004/parts/0041345403/modules/750849864075460/lessons/7600631235/concepts/483298610923#" target="_blank">demo</a> for more details.</li>
</ul>
<h2 id="step-4-add-logout">Step 4: Add Logout</h2>
<ul>
<li>Have a logout form that validates user input, and displays the error(s) when necessary.</li>
<li>After logging out, the cookie is cleared and user is redirected to the Signup page from Step 2.</li>
<li>Watch the <a href="https://classroom.udacity.com/nanodegrees/nd004/parts/0041345403/modules/750849864075460/lessons/7600631235/concepts/482965550923#" target="_blank">demo</a> for more details.</li>
</ul>
<h2 id="step-5-add-other-features-on-your-own">Step 5: Add Other Features on Your Own</h2>
<ul>
<li>Users should only be able to edit/delete their posts. They receive an error message if they disobey this rule.</li>
<li>Users can like/unlike posts, but not their own. They receive an error message if they disobey this rule.</li>
<li>Users can comment on posts. They can only edit/delete their own posts, and they should receive an error message if they disobey this rule.</li>
</ul>
<h2 id="step-6-final-touches">Step 6: Final Touches</h2>
<ul>
<li>Create a README.md file explaining how to run your code.</li>
<li>Refactor your code so it is well structured, well commented, and conforms to the <a href="https://www.python.org/dev/peps/pep-0008/" target="_blank">Python Style Guide</a>.</li>
<li>Make sure your project conforms to the <a href="https://review.udacity.com/#!/projects/7508498640/rubric" target="_blank">rubric</a>.</li>
<li>Deploy your app to appspot.com using <code>gcloud app deploy</code>.</li>
<li><a href="https://review.udacity.com/#!/projects/150/start" target="_blank">Submit your project</a>.</li>
<li>Revise your project and resubmit as necessary.</li>
<li>Pat yourself on the back!</li>
</ul>
</div>

# Rubric

<div id="proj-spec-div" class="col-xs-offset-1 col-xs-10"> <h2 id="project-spec-headline" translate="" class="ng-scope">Project Specification</h2> <h3 id="project-name" ng-bind-html="localize(ctrl.rubric.project, 'name', markup=true)" class="ng-binding"><p>Multi User Blog</p>
</h3>  <!-- ngRepeat: section in ctrl.rubric.sections --><div ng-repeat="section in ctrl.rubric.sections" class="ng-scope" style=""> <span class="rubric-section ng-binding" ng-bind-html="localize(section, 'name', markup=true)"><p>Code Functionality</p>
</span> <table class="table table-bordered section-table"> <thead> <tr> <!-- ngIf: !ctrl.hideCriteria --><th class="rubric-category criteria col-xs-3 ng-scope" ng-if="!ctrl.hideCriteria"> <span translate="" class="ng-scope">Criteria</span> </th><!-- end ngIf: !ctrl.hideCriteria --> <th class="rubric-category meets-specs" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4"> <span translate="" class="ng-scope">Meets Specifications</span> </th> <!-- ngIf: ctrl.reviewerTips --> </tr> </thead> <tbody>  <!-- ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>What framework is used?</p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>App is built using Google App Engine</p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>Blog is deployed and viewable to the public.</p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>The submitted URL is publicly accessible.</p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --> </tbody> </table> </div><!-- end ngRepeat: section in ctrl.rubric.sections --><div ng-repeat="section in ctrl.rubric.sections" class="ng-scope"> <span class="rubric-section ng-binding" ng-bind-html="localize(section, 'name', markup=true)"><p>Site Usability</p>
</span> <table class="table table-bordered section-table"> <thead> <tr> <!-- ngIf: !ctrl.hideCriteria --><th class="rubric-category criteria col-xs-3 ng-scope" ng-if="!ctrl.hideCriteria"> <span translate="" class="ng-scope">Criteria</span> </th><!-- end ngIf: !ctrl.hideCriteria --> <th class="rubric-category meets-specs" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4"> <span translate="" class="ng-scope">Meets Specifications</span> </th> <!-- ngIf: ctrl.reviewerTips --> </tr> </thead> <tbody>  <!-- ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>The signup, login, and logout workflow is intuitive to a human user.</p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>User is directed to login, logout, and signup pages as appropriate. E.g., login page should have a link to signup page and vice-versa; logout page is only available to logged in user.</p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>Editing and viewing workflow is intuitive to a human user.</p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>Links to edit blog pages are available to users. Users editing a page can click on a link to cancel the edit and go back to viewing that page. </p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>Pages render correctly.</p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>Blog pages render properly. Templates are used to unify the site. </p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --> </tbody> </table> </div><!-- end ngRepeat: section in ctrl.rubric.sections --><div ng-repeat="section in ctrl.rubric.sections" class="ng-scope"> <span class="rubric-section ng-binding" ng-bind-html="localize(section, 'name', markup=true)"><p>Accounts and Security</p>
</span> <table class="table table-bordered section-table"> <thead> <tr> <!-- ngIf: !ctrl.hideCriteria --><th class="rubric-category criteria col-xs-3 ng-scope" ng-if="!ctrl.hideCriteria"> <span translate="" class="ng-scope">Criteria</span> </th><!-- end ngIf: !ctrl.hideCriteria --> <th class="rubric-category meets-specs" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4"> <span translate="" class="ng-scope">Meets Specifications</span> </th> <!-- ngIf: ctrl.reviewerTips --> </tr> </thead> <tbody>  <!-- ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>User accounts are appropriately handled.</p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>Users are able to create accounts, login, and logout correctly.</p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>Account information is properly retained.</p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>Existing users can revisit the site and log back in without having to recreate their accounts each time.</p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>Usernames are unique. </p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>Usernames are unique. Attempting to create a duplicate user results in an error message.</p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>Passwords are secure and appropriately used.</p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>Stored passwords are hashed. Passwords are appropriately checked during login. User cookie is set securely.</p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --> </tbody> </table> </div><!-- end ngRepeat: section in ctrl.rubric.sections --><div ng-repeat="section in ctrl.rubric.sections" class="ng-scope"> <span class="rubric-section ng-binding" ng-bind-html="localize(section, 'name', markup=true)"><p>Permissions</p>
</span> <table class="table table-bordered section-table"> <thead> <tr> <!-- ngIf: !ctrl.hideCriteria --><th class="rubric-category criteria col-xs-3 ng-scope" ng-if="!ctrl.hideCriteria"> <span translate="" class="ng-scope">Criteria</span> </th><!-- end ngIf: !ctrl.hideCriteria --> <th class="rubric-category meets-specs" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4"> <span translate="" class="ng-scope">Meets Specifications</span> </th> <!-- ngIf: ctrl.reviewerTips --> </tr> </thead> <tbody>  <!-- ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>User permissions are appropriate for logged out users.</p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>Logged out users are redirected to the login page when attempting to create, edit, delete, or like a blog post.</p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>User permissions are appropriate for logged in users.</p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>Logged in users can create, edit, or delete blog posts they themselves have created. </p>
<p>Users should only be able to like posts once and should not be able to like their own post.</p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>Comment permissions are enforced.</p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>Only signed in users can post comments.<br>Users can only edit and delete comments they themselves have made.</p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --> </tbody> </table> </div><!-- end ngRepeat: section in ctrl.rubric.sections --><div ng-repeat="section in ctrl.rubric.sections" class="ng-scope"> <span class="rubric-section ng-binding" ng-bind-html="localize(section, 'name', markup=true)"><p>Code Quality</p>
</span> <table class="table table-bordered section-table"> <thead> <tr> <!-- ngIf: !ctrl.hideCriteria --><th class="rubric-category criteria col-xs-3 ng-scope" ng-if="!ctrl.hideCriteria"> <span translate="" class="ng-scope">Criteria</span> </th><!-- end ngIf: !ctrl.hideCriteria --> <th class="rubric-category meets-specs" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4"> <span translate="" class="ng-scope">Meets Specifications</span> </th> <!-- ngIf: ctrl.reviewerTips --> </tr> </thead> <tbody>  <!-- ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>Code should be readable per the Google <a href="https://google.github.io/styleguide/pyguide.html" target="_blank">Python Style Guide</a>.</p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>Code follows the Google Python Style Guide. </p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>Code is well structured.</p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>Code follows an intuitive, easy-to-follow logical structure.</p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>Code is well commented.</p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>Code that is not intuitively readable is well-documented with comments.</p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --> </tbody> </table> </div><!-- end ngRepeat: section in ctrl.rubric.sections --><div ng-repeat="section in ctrl.rubric.sections" class="ng-scope"> <span class="rubric-section ng-binding" ng-bind-html="localize(section, 'name', markup=true)"><p>Documentation</p>
</span> <table class="table table-bordered section-table"> <thead> <tr> <!-- ngIf: !ctrl.hideCriteria --><th class="rubric-category criteria col-xs-3 ng-scope" ng-if="!ctrl.hideCriteria"> <span translate="" class="ng-scope">Criteria</span> </th><!-- end ngIf: !ctrl.hideCriteria --> <th class="rubric-category meets-specs" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4"> <span translate="" class="ng-scope">Meets Specifications</span> </th> <!-- ngIf: ctrl.reviewerTips --> </tr> </thead> <tbody>  <!-- ngRepeat: rubricItem in section.rubric_items --><tr ng-repeat="rubricItem in section.rubric_items" class="ng-scope"> <!-- ngIf: !ctrl.hideCriteria --><td class="rubric-item col-xs-3 ng-binding ng-scope" ng-if="!ctrl.hideCriteria" ng-bind-html="localize(rubricItem, 'criteria', markup=true)"><p>Are steps for running the project provided in a README file?</p>
</td><!-- end ngIf: !ctrl.hideCriteria --> <td class="rubric-item ng-binding" ng-class="ctrl.reviewerTips ? col-xs-7 : col-xs-4" ng-bind-html="localize(rubricItem, 'passed_description', markup=true)"><p>Instructions on how to run the project are outlined in a README file.</p>
</td> <!-- ngIf: ctrl.reviewerTips --> </tr><!-- end ngRepeat: rubricItem in section.rubric_items --> </tbody> </table> </div><!-- end ngRepeat: section in ctrl.rubric.sections --> <!-- ngIf: ctrl.rubric.stand_out --> </div>
