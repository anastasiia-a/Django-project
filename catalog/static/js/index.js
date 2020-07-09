$(document).ready(function() {

    $("#button").click(function () {
        var data = $("#text_search").val();
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        console.log(data)
        $.ajax({
            type: "POST",
            data: {search: data},
            url: '/search/',
            beforeSend: function(xhr, settings) {xhr.setRequestHeader("X-CSRFToken", csrftoken);},
            success: function (response) {
                $(".content").html(response.html)
            }
        })
    }
)
    $(".cat").on('click', function (event) {
        event.preventDefault();

        var data = ($(this).attr('href'));
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        $("#text").val('');
        console.log(data)

        $.ajax({
            type: "POST",
            data: {category: data},
            url: data,
            beforeSend: function(xhr, settings) {xhr.setRequestHeader("X-CSRFToken", csrftoken);},
            success: function (response) {
                $(".content").html(response.html)
                history.pushState({}, 'Catalog', data);
            }
        })
    })

    $(".product").on('click', function (event) {
        event.preventDefault();
        var data = ($(this).attr('href'));
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        $("#text").val('');

        $.ajax({
            type: "POST",
            data: {category: data},
            url: data,
            beforeSend: function(xhr, settings) {xhr.setRequestHeader("X-CSRFToken", csrftoken);},
            success: function (response) {
                $(".content").html(response.html)
                history.pushState({}, 'Сatalog', data)
            }
        })
    })
});
