# Securly-Extension-Spammer
A spammer to send mass emails to teachers. (Education Purposes only!)
# Setup
Just go a securly blocked page(You can do this by going to a blocked website like https://discord.com) then press inspect element. On the element tab search for the paramatars that look like this
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
Copy and paste this into the console
```
    function sendEmail(obj){
        $.post( "app/api/sendtwl",obj)
            .done(function( data ) {
                window.scroll(0,0);
                resetFormDetails();
                $("#mailSuccess").text(data.message);
                $("#mailSuccess").show();
                setTimeout(function(){
                    $("#mailSuccess").hide();
                }, 5000);
            })
            .fail(function(error){
                window.scroll(0,0);
                resetFormDetails();
                $("#mailSuccess").text(error.message);
                $("#mailSuccess").show();
                $("#mailSuccess").css('background','#fd9292');
                setTimeout(function(){
                    $("#mailSuccess").hide();
                    $("#mailSuccess").css('background','#28d9c3');
                }, 5000);
            });
    }

    function resetFormDetails(){
        $("#contactAdminForm")[0].reset();
        $("#sendEmail").attr("disabled", true);
        $('#otherReasonInfo').hide();
    }
```
Then copy the part of the code you found earlier and paste it into the console.
It should look something like this
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
Then type ``` sendEmail(params); ``` and hit enter
Go to the network tab inside inspect element and click the sendtwl scroll down to the form data and copy the emails, reason and all the other stuff
Go into the python and code and replace the email with your schools admin email that you got from the network tab.
Run the code and boom your done
