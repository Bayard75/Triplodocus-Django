let ajoutForm = document.getElementById('form_ajout')

// Hiding the logged as
document.getElementById('embed-api-auth-container').style.display = 'none';

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
    let spotifyValue = document.getElementById('id_spotify')
    youtubeValue.value = youtubeValue.value.replace('watch?v=','embed/')
    spotifyValue.value = spotifyValue.value.replace('/album/','/embed/album/')
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

