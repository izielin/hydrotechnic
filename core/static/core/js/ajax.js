$("form").not('#offerForm', '#boxForm').change(function (event) {
    event.preventDefault();
    let my_form = $(this).closest("form");
    let data = new FormData(my_form[0]);
    $.ajax({
        url: $(this).attr('data-url_root'),
        type: 'POST',
        data: data,
        cache: false,
        processData: false,
        contentType: false,
        success: function (data) {

        },
        error: function (xhr, errmsg, err) {
        }
    });
});