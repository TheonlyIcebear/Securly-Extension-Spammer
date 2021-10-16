# Securly-Extension-Spammer
A spammer to send mass emails to teachers. (Education Purposes only!)
# Setup
Just go a securly blocked page then press inspect element. On the element tab search for the paramatars that look like this
```
        $('#sendEmail').click(function(ev){
            // Disabled send button once clicked.
            $("#sendEmail").attr("disabled", true);
            var params={};
            params['site']= $('#permissionSite').val();
            params['teacherEmail']= $('#teacherEmail').val();
            params['reason']= $('#questionSelection').val();
            params['otherReason']= $('#otherReasonInfo').val();
            params['categories'] = "Games";
            params['keyword'] = "";
            params['blockedReason'] = "site";
            params['policy'] = "Base/Default Policy";
            params['requesterOU'] = "-";
            params['requesterSafeSecGroupName'] = "-";
            params['requester'] = "TeachersEmailGoesHere";
            params['fid'] = "TeachersEmailGoesHere";
            params['i2n'] = "";
            sendEmail(params);
```
Copy everything inside the <script> tags and then paste it into the console. Then copy this part of the code
```
            var params={};
            params['site']= $('#permissionSite').val();
            params['teacherEmail']= $('#teacherEmail').val();
            params['reason']= $('#questionSelection').val();
            params['otherReason']= $('#otherReasonInfo').val();
            params['categories'] = "Games";
            params['keyword'] = "";
            params['blockedReason'] = "site";
            params['policy'] = "Base/Default Policy";
            params['requesterOU'] = "-";
            params['requesterSafeSecGroupName'] = "-";
            params['requester'] = "TeachersEmailGoesHere";
            params['fid'] = "TeachersEmailGoesHere";
            params['i2n'] = "";
```
Then type ``` sendEmail(params); ```
Go to the network tab inside inspect element and click the sendtwl scroll down to the form data and copy the emails, reason and all the other stuff
Go into the python and code and replace the email with your schools admin email that you got from the network tab.
Run the code and boom your done
