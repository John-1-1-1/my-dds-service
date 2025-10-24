 document.addEventListener('DOMContentLoaded', function() {
    const editModal = document.getElementById('editModal');
    const editForm = document.getElementById('editForm');
    const editModalBody = document.getElementById('editModalBody');
    const modalTitle = document.getElementById('editModalLabel');

    let currentRowToUpdate = null;

    if (editModal) {
        editModal.addEventListener('show.bs.modal', function (event) {
            const button = event.relatedTarget;
            const editUrl = button.getAttribute('data-edit-url');
            const objectName = button.getAttribute('data-object-name');
            const isCreate = button.getAttribute('data-is-create') === 'true';

            if (isCreate) {
                modalTitle.textContent = `Создание: ${editUrl.split('/')[1] || 'Объекта'}`;
            } else {
                modalTitle.textContent = `Редактирование: ${objectName}`;
                currentRowToUpdate = button.closest('tr');
            }

            fetch(editUrl)
                .then(response => response.text())
                .then(html => {
                    editModalBody.innerHTML = html;
                    editForm.action = editUrl;

                    const innerFormButton = editModalBody.querySelector('button[type="submit"]');
                    if (innerFormButton) {
                        innerFormButton.style.display = 'none';
                    }
                })
                .catch(error => {
                    editModalBody.innerHTML = `<p class="text-danger">Ошибка загрузки формы.</p>`;
                    console.error('Ошибка загрузки:', error);
                });
        });

        editForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const formData = new FormData(editForm);

            fetch(editForm.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                }
            })
            .then(response => {
                if (response.ok && !response.redirected) {
                    var modal = bootstrap.Modal.getInstance(editModal);
                    modal.hide();
                    window.location.reload();

                } else if (response.redirected) {
                    var modal = bootstrap.Modal.getInstance(editModal);
                    modal.hide();
                    window.location.reload();
                } else {
                    return response.text();
                }
            })
            .then(html => {
                if (html) {
                    editModalBody.innerHTML = html;
                    const innerFormButton = editModalBody.querySelector('button[type="submit"]');
                    if (innerFormButton) {
                        innerFormButton.style.display = 'none';
                    }
                }
            })
            .catch(error => console.error('Ошибка сохранения:', error));
        });
    }
});