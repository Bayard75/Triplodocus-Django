let ajoutForm = document.getElementById('form_ajout')

function displayBadges(deleteId, editId)
{
    document.getElementById(deleteId).style.visibility = 'visible';
    document.getElementById(editId).style.visibility = 'visible';
}
function hideBadges(deleteId, editId)
{
    document.getElementById(deleteId).style.visibility = 'hidden';
    document.getElementById(editId).style.visibility = 'hidden';

}

function showModalSuppression(id_to_delete)
{
    let target = id_to_delete.slice(13);
    document.getElementById("modal_suppression").className ="modal fade show";
    document.getElementById("modal_suppression").style.display ="block";

}

function deleteSong(id)
{
    let body = {id: id}

    let host = window.location.origin;
    let delete_page = new URL('/delete_song',host)
    
    document.getElementById('button_supprimer').addEventListener('click',function(event)
    {
        fetch(delete_page,{
            method: 'POST',
            headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken':'{{csrf_token}}',
            'X-Requested-With':'XMLHttpRequest' 
            },

            body:JSON.stringify(body),
            mode:'cors',
            cache:'default',
            credentials:'include'     
        })
        .then((reponse)=>{
            document.getElementById('hide_span').click()
            document.getElementById(id + '_col').style.display = 'none'
        })
    })

}
ajoutForm.addEventListener('submit',function(event)
{
    let youtubeValue = document.getElementById('id_youtube')
    youtubeValue.value = youtubeValue.value.replace('watch?v=','embed/')
})

function changeEnAvant(id)
{
    let body = {id: id.slice(7)}

    let host = window.location.origin;
    let change_page = new URL('/change_en_avant',host)
    
    
    fetch(change_page,{
            method: 'POST',
            headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken':'{{csrf_token}}',
            'X-Requested-With':'XMLHttpRequest' 
            },

            body:JSON.stringify(body),
            mode:'cors',
            cache:'default',
            credentials:'include'     
        })
        .then((reponse)=>{
            return reponse.json()
        })
        .then((data)=>{
            if (data['message'])
            {
                alert(data['message'])
                document.getElementById(id).checked = false

            }
            else
            {
                document.getElementById(id).checked = true
                let ancien_id = 'switch_'+data['ancient']
                document.getElementById(ancien_id).checked = false
            }

        })   
}

gapi.analytics.ready(function() {

    /**
     * Authorize the user immediately if the user has already granted access.
     * If no access has been created, render an authorize button inside the
     * element with the ID "embed-api-auth-container".
     */
    gapi.analytics.auth.authorize({
      container: 'embed-api-auth-container',
      clientid: 'REPLACE WITH YOUR CLIENT ID'
    });
  
  
    /**
     * Create a new ViewSelector instance to be rendered inside of an
     * element with the id "view-selector-container".
     */
    var viewSelector = new gapi.analytics.ViewSelector({
      container: 'view-selector-container'
    });
  
    // Render the view selector to the page.
    viewSelector.execute();
  
  
    /**
     * Create a new DataChart instance with the given query parameters
     * and Google chart options. It will be rendered inside an element
     * with the id "chart-container".
     */
    var dataChart = new gapi.analytics.googleCharts.DataChart({
      query: {
        metrics: 'ga:sessions',
        dimensions: 'ga:date',
        'start-date': '30daysAgo',
        'end-date': 'yesterday'
      },
      chart: {
        container: 'chart-container',
        type: 'LINE',
        options: {
          width: '100%'
        }
      }
    });
  
  
    /**
     * Render the dataChart on the page whenever a new view is selected.
     */
    viewSelector.on('change', function(ids) {
      dataChart.set({query: {ids: ids}}).execute();
    });
  
  });