$("form").change(function (event) {
    event.preventDefault();
    let form = $(this).closest("form");
    $.ajax({
        url: form.attr("data-url_root"),
        data: form.serialize(),
        dataType: 'json',
        success: function (json) {
        },
        error: function (xhr, errmsg, err) {
        }
    });
});