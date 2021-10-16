# Securly-Extension-Spammer
A spammer to send mass emails to teachers. (Education Purposes only!)
# Setup
Just go a securly blocked page then press inspect element. Search for the paramatars that look like this
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
            params['requester'] = "amogus@willnorth.org";
            params['fid'] = "administrator@willnorth.org";
            params['i2n'] = "";
            sendEmail(params);
```
