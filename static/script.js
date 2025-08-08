document.getElementById('saveBtn').onclick = function() {
    const mapping = {};
    document.querySelectorAll('input[data-emoji-id]').forEach(input => {
        const val = input.value.trim();
        if (val) {
            mapping[input.dataset.emojiId] = val;
        }
    });

    if (Object.keys(mapping).length === 0) {
      alert("You haven't entered any names.");
      return;
    }

    const blob = new Blob([JSON.stringify(mapping, null, 2)], { type: 'application/json' });
    const a = document.createElement('a');
    
    a.href = URL.createObjectURL(blob);
    a.download = 'mapped_emoji.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(a.href);

    alert('The file "mapped_emoji.json" has been saved successfully!');
};