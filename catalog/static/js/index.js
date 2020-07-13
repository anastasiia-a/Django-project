$(document).ready(function begin() {
    $('#button').on('click', function (event) {
        var text = $('#text_search').val();
        var csrftoken = $('[name=csrfmiddlewaretoken]').val();

        $.ajax({
            type: 'GET',
            data: {search: text},
            url: '/search',
            beforeSend: function(xhr, settings) {xhr.setRequestHeader("X-CSRFToken", csrftoken);},
            success: function (response) {
                $(".content").html(response.html)
                history.pushState({}, 'Catalog', '/search/'+text);
                begin();

            }
        })
    })
    $('.pag_button').on('click', function test (event) {
        event.preventDefault();
        var text = $('#text_search').val();
        var csrftoken = $('[name=csrfmiddlewaretoken]').val();
        var data = ($(this).attr('href'));

        $.ajax({
            type: 'GET',
            data: {search: text},
            url: data,
            beforeSend: function(xhr, settings) {xhr.setRequestHeader("X-CSRFToken", csrftoken);},
            success: function (response) {
                $(".content").html(response.html)
                history.pushState({}, 'Catalog', data);
                begin();
            }
        })
    })
    $('.cat').on('click', function (event) {
        event.preventDefault();
        var data = ($(this).attr('href'));
        var csrftoken = $('[name=csrfmiddlewaretoken]').val();

        $.ajax({
            type: 'POST',
            data: {category: data},
            url: data,
            beforeSend: function(xhr, settings) {xhr.setRequestHeader('X-CSRFToken', csrftoken);},
            success: function (response) {
                $(".content").html(response.html)
                history.pushState({}, 'Catalog', data);
                begin();

            }
        })
    })
    $('.product').on('click', function (event) {
        event.preventDefault();
        var data = ($(this).attr('href'));
        var csrftoken = $('[name=csrfmiddlewaretoken]').val();

        $.ajax({
            type: 'POST',
            data: {category: data},
            url: data,
            beforeSend: function(xhr, settings) {xhr.setRequestHeader('X-CSRFToken', csrftoken);},
            success: function (response) {
                $('.content').html(response.html)
                history.pushState({}, 'Сatalog', data);
                begin();
            }
        })
    })
});
