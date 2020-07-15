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

