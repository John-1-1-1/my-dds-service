  document.addEventListener('DOMContentLoaded', function() {
        const deleteConfirmModal = document.getElementById('deleteConfirmModal');

        if (deleteConfirmModal) {
            deleteConfirmModal.addEventListener('show.bs.modal', function (event) {
                const button = event.relatedTarget;

                const objectId = button.getAttribute('data-object-id');
                const objectName = button.getAttribute('data-object-name');
                const deleteUrl = button.getAttribute('data-delete-url-name');

                const modalForm = document.getElementById('deleteForm');
                const objectIdPlaceholder = document.getElementById('objectIdPlaceholder');
                const objectNamePlaceholder = document.getElementById('objectNamePlaceholder');

                modalForm.setAttribute('action', deleteUrl);

                objectIdPlaceholder.textContent = objectId;
                objectNamePlaceholder.textContent = objectName;
            });
        }
    });
