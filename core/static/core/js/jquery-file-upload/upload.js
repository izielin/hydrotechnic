$(function () {

    $(".js-upload-photos").click(function () {
        $("#fileupload").click();
    });

    $("#fileupload").fileupload({
        dataType: 'json',
        sequentialUploads: true,
        start: function (e) {
            $("#modal-progress").modal("show");
        },
        stop: function (e) {
            $("#modal-progress").modal("hide");
        },
        progressall: function (e, data) {
            let progress = parseInt(data.loaded / data.total * 100, 10);
            let strProgress = progress + "%";
            $(".progress-bar").css({"width": strProgress});
            $(".progress-bar").text(strProgress);
        },
        done: function (e, data) {
            if (data.result.is_valid) {
                $("#gallery tbody").prepend(
                    "<tr><td><div class=\"row\">"
                    + "<div class=\"col\"><img src=\" " + data.result.url + " \" style=\"max-height: 100px;\" alt=\"\">"
                    + "</div>"
                    + "</div></td></tr>"
                )
            }
        }

    });

});