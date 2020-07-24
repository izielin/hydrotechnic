$("form").not('#boxForm').change(function (event) {
    event.preventDefault();
    let data = new FormData($(this).get(0));
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