# Create an interactive drag-and-drop web application for IELTS vocabulary exercise
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IELTS Vocabulary Exercise - Addition, Equation & Conclusion</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            padding: 30px;
        }
        
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        
        .header h1 {
            color: #333;
            margin-bottom: 10px;
            font-size: 2.2em;
        }
        
        .header p {
            color: #666;
            font-size: 1.1em;
        }
        
        .instructions {
            background: #f8f9ff;
            border-left: 4px solid #667eea;
            padding: 15px;
            margin-bottom: 25px;
            border-radius: 5px;
        }
        
        .word-bank {
            background: #fff5f5;
            border: 2px dashed #ff6b6b;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 25px;
            min-height: 100px;
        }
        
        .word-bank h3 {
            margin-top: 0;
            color: #ff6b6b;
            text-align: center;
        }
        
        .words-container {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
        }
        
        .word-item {
            background: #4ecdc4;
            color: white;
            padding: 8px 15px;
            border-radius: 25px;
            cursor: grab;
            user-select: none;
            transition: all 0.3s ease;
            font-weight: 500;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }
        
        .word-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            background: #45b7aa;
        }
        
        .word-item.dragging {
            opacity: 0.5;
            transform: rotate(5deg);
        }
        
        .categories {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-bottom: 25px;
        }
        
        .category {
            border: 2px solid #ddd;
            border-radius: 10px;
            min-height: 200px;
            padding: 15px;
            background: #fafafa;
            transition: all 0.3s ease;
        }
        
        .category.drag-over {
            border-color: #4ecdc4;
            background: #f0fdfc;
            transform: scale(1.02);
        }
        
        .category h3 {
            text-align: center;
            margin-top: 0;
            padding: 10px;
            border-radius: 8px;
            color: white;
            font-size: 1.2em;
        }
        
        .category.addition h3 {
            background: #ff6b6b;
        }
        
        .category.equation h3 {
            background: #4ecdc4;
        }
        
        .category.conclusion h3 {
            background: #45b7aa;
        }
        
        .category-items {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            min-height: 150px;
            padding: 10px;
            border: 1px dashed #ccc;
            border-radius: 5px;
            background: white;
        }
        
        .placed-word {
            background: #95a5a6;
            color: white;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.9em;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .placed-word:hover {
            background: #7f8c8d;
            transform: translateY(-1px);
        }
        
        .placed-word.correct {
            background: #2ecc71;
            animation: correctPulse 0.5s ease;
        }
        
        .placed-word.incorrect {
            background: #e74c3c;
            animation: incorrectShake 0.5s ease;
        }
        
        @keyframes correctPulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        
        @keyframes incorrectShake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-5px); }
            75% { transform: translateX(5px); }
        }
        
        .controls {
            text-align: center;
            margin-top: 25px;
        }
        
        .btn {
            background: #667eea;
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 1em;
            margin: 0 10px;
            transition: all 0.3s ease;
            box-shadow: 0 3px 10px rgba(0,0,0,0.2);
        }
        
        .btn:hover {
            background: #5a6fd8;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }
        
        .btn:active {
            transform: translateY(0);
        }
        
        .feedback {
            text-align: center;
            margin-top: 20px;
            padding: 15px;
            border-radius: 10px;
            font-weight: bold;
            font-size: 1.1em;
        }
        
        .feedback.show {
            display: block;
        }
        
        .feedback.hide {
            display: none;
        }
        
        .feedback.success {
            background: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        
        .feedback.error {
            background: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
        
        .score {
            text-align: center;
            font-size: 1.2em;
            color: #333;
            margin-bottom: 20px;
        }
        
        .progress-bar {
            width: 100%;
            height: 10px;
            background: #e0e0e0;
            border-radius: 5px;
            margin: 15px 0;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(45deg, #4ecdc4, #44a08d);
            width: 0%;
            transition: width 0.3s ease;
            border-radius: 5px;
        }
        
        @media (max-width: 768px) {
            .categories {
                grid-template-columns: 1fr;
            }
            
            .container {
                padding: 20px;
            }
            
            .header h1 {
                font-size: 1.8em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯 IELTS Vocabulary Exercise</h1>
            <p>Day 1: Addition, Equation & Conclusion</p>
        </div>
        
        <div class="instructions">
            <strong>Instructions:</strong> Drag and drop the words/phrases into the correct categories:<br>
            • <strong>Addition:</strong> Words that add information<br>
            • <strong>Equation:</strong> Words that show similarity/comparison<br>
            • <strong>Conclusion:</strong> Words that conclude or summarize
        </div>
        
        <div class="score">
            <span>Score: <span id="score">0</span>/24</span>
            <div class="progress-bar">
                <div class="progress-fill" id="progress"></div>
            </div>
        </div>
        
        <div class="word-bank" id="wordBank">
            <h3>📝 Word Bank - Drag these words to the correct categories</h3>
            <div class="words-container" id="wordsContainer">
                <!-- Words will be populated here -->
            </div>
        </div>
        
        <div class="categories">
            <div class="category addition" data-category="addition">
                <h3>Addition</h3>
                <div class="category-items" id="addition-items"></div>
            </div>
            
            <div class="category equation" data-category="equation">
                <h3>Equation</h3>
                <div class="category-items" id="equation-items"></div>
            </div>
            
            <div class="category conclusion" data-category="conclusion">
                <h3>Conclusion</h3>
                <div class="category-items" id="conclusion-items"></div>
            </div>
        </div>
        
        <div class="controls">
            <button class="btn" onclick="checkAnswers()">✓ Check Answers</button>
            <button class="btn" onclick="resetExercise()">🔄 Reset</button>
            <button class="btn" onclick="showHint()">💡 Hint</button>
        </div>
        
        <div class="feedback hide" id="feedback"></div>
    </div>

    <script>
        // Word definitions and correct answers
        const wordsData = {
            'along with': 'addition',
            'also': 'addition',
            'and': 'addition',
            'as well as': 'addition',
            'besides': 'addition',
            'furthermore': 'addition',
            'in addition': 'addition',
            'moreover': 'addition',
            'too': 'addition',
            'what\\'s more': 'addition',
            'correspondingly': 'equation',
            'equally': 'equation',
            'in the same way': 'equation',
            'likewise': 'equation',
            'similarly': 'equation',
            'in brief': 'conclusion',
            'in conclusion': 'conclusion',
            'thus': 'conclusion',
            'therefore': 'conclusion',
            'to conclude': 'conclusion',
            'to summarise': 'conclusion',
            'to sum up': 'conclusion',
            'briefly': 'conclusion',
            'we can conclude that': 'conclusion'
        };
        
        let score = 0;
        let currentAnswers = {};
        
        // Initialize the exercise
        function initializeExercise() {
            const wordsContainer = document.getElementById('wordsContainer');
            wordsContainer.innerHTML = '';
            
            // Shuffle words for variety
            const words = Object.keys(wordsData);
            const shuffledWords = words.sort(() => Math.random() - 0.5);
            
            shuffledWords.forEach(word => {
                const wordElement = document.createElement('div');
                wordElement.className = 'word-item';
                wordElement.draggable = true;
                wordElement.textContent = word;
                wordElement.dataset.word = word;
                
                // Drag event listeners
                wordElement.addEventListener('dragstart', handleDragStart);
                wordElement.addEventListener('dragend', handleDragEnd);
                
                wordsContainer.appendChild(wordElement);
            });
            
            // Reset categories
            ['addition', 'equation', 'conclusion'].forEach(category => {
                document.getElementById(category + '-items').innerHTML = '';
            });
            
            // Reset score and feedback
            score = 0;
            updateScore();
            currentAnswers = {};
            document.getElementById('feedback').className = 'feedback hide';
        }
        
        // Drag and drop handlers
        function handleDragStart(e) {
            e.dataTransfer.setData('text/plain', e.target.dataset.word);
            e.target.classList.add('dragging');
        }
        
        function handleDragEnd(e) {
            e.target.classList.remove('dragging');
        }
        
        // Set up drop zones
        document.addEventListener('DOMContentLoaded', function() {
            initializeExercise();
            
            // Add drop event listeners to categories
            const categories = document.querySelectorAll('.category-items');
            categories.forEach(category => {
                category.addEventListener('dragover', handleDragOver);
                category.addEventListener('drop', handleDrop);
                category.addEventListener('dragenter', handleDragEnter);
                category.addEventListener('dragleave', handleDragLeave);
            });
        });
        
        function handleDragOver(e) {
            e.preventDefault();
        }
        
        function handleDragEnter(e) {
            e.preventDefault();
            e.target.closest('.category').classList.add('drag-over');
        }
        
        function handleDragLeave(e) {
            if (!e.target.closest('.category').contains(e.relatedTarget)) {
                e.target.closest('.category').classList.remove('drag-over');
            }
        }
        
        function handleDrop(e) {
            e.preventDefault();
            const word = e.dataTransfer.getData('text/plain');
            const category = e.target.closest('.category').dataset.category;
            
            // Remove drag-over effect
            e.target.closest('.category').classList.remove('drag-over');
            
            // Find and remove the word from its current location
            const wordElement = document.querySelector(`[data-word="${word}"]`);
            if (wordElement) {
                wordElement.remove();
            }
            
            // Remove word from previous category if it was already placed
            Object.keys(currentAnswers).forEach(cat => {
                if (currentAnswers[cat] && currentAnswers[cat].includes(word)) {
                    currentAnswers[cat] = currentAnswers[cat].filter(w => w !== word);
                }
            });
            
            // Add word to new category
            if (!currentAnswers[category]) {
                currentAnswers[category] = [];
            }
            currentAnswers[category].push(word);
            
            // Create placed word element
            const placedWord = document.createElement('div');
            placedWord.className = 'placed-word';
            placedWord.textContent = word;
            placedWord.dataset.word = word;
            placedWord.onclick = () => returnWordToBank(word);
            
            e.target.appendChild(placedWord);
            
            updateScore();
        }
        
        function returnWordToBank(word) {
            // Remove from categories
            Object.keys(currentAnswers).forEach(cat => {
                if (currentAnswers[cat] && currentAnswers[cat].includes(word)) {
                    currentAnswers[cat] = currentAnswers[cat].filter(w => w !== word);
                }
            });
            
            // Remove from DOM
            const placedElements = document.querySelectorAll(`[data-word="${word}"]`);
            placedElements.forEach(el => {
                if (el.classList.contains('placed-word')) {
                    el.remove();
                }
            });
            
            // Add back to word bank
            const wordElement = document.createElement('div');
            wordElement.className = 'word-item';
            wordElement.draggable = true;
            wordElement.textContent = word;
            wordElement.dataset.word = word;
            wordElement.addEventListener('dragstart', handleDragStart);
            wordElement.addEventListener('dragend', handleDragEnd);
            
            document.getElementById('wordsContainer').appendChild(wordElement);
            
            updateScore();
        }
        
        function updateScore() {
            let correct = 0;
            const totalWords = Object.keys(wordsData).length;
            
            Object.keys(currentAnswers).forEach(category => {
                if (currentAnswers[category]) {
                    currentAnswers[category].forEach(word => {
                        if (wordsData[word] === category) {
                            correct++;
                        }
                    });
                }
            });
            
            score = correct;
            document.getElementById('score').textContent = score;
            
            const progressPercent = (score / totalWords) * 100;
            document.getElementById('progress').style.width = progressPercent + '%';
        }
        
        function checkAnswers() {
            let feedback = '';
            let allCorrect = true;
            
            // Clear previous styling
            document.querySelectorAll('.placed-word').forEach(word => {
                word.classList.remove('correct', 'incorrect');
            });
            
            Object.keys(currentAnswers).forEach(category => {
                if (currentAnswers[category]) {
                    currentAnswers[category].forEach(word => {
                        const wordElement = document.querySelector(`#${category}-items [data-word="${word}"]`);
                        if (wordsData[word] === category) {
                            wordElement.classList.add('correct');
                        } else {
                            wordElement.classList.add('incorrect');
                            allCorrect = false;
                        }
                    });
                }
            });
            
            const totalWords = Object.keys(wordsData).length;
            const placedWords = Object.values(currentAnswers).flat().length;
            
            if (placedWords === 0) {
                feedback = 'Please place some words in the categories first!';
                showFeedback(feedback, 'error');
            } else if (allCorrect && score === totalWords) {
                feedback = `🎉 Excellent! Perfect score ${score}/${totalWords}! You've mastered IELTS linking words for Addition, Equation, and Conclusion. This vocabulary will significantly boost your Writing Task 2 coherence and cohesion scores!`;
                showFeedback(feedback, 'success');
            } else if (score >= totalWords * 0.8) {
                feedback = `👍 Great work! Score: ${score}/${totalWords}. You have a strong understanding of IELTS linking vocabulary. Review the incorrect ones and you'll be ready for Band 7.5+!`;
                showFeedback(feedback, 'success');
            } else {
                feedback = `📚 Keep practicing! Score: ${score}/${totalWords}. Focus on understanding the function of each linking word. Remember: Addition words add information, Equation words show similarity, Conclusion words summarize or conclude.`;
                showFeedback(feedback, 'error');
            }
        }
        
        function showFeedback(message, type) {
            const feedbackElement = document.getElementById('feedback');
            feedbackElement.textContent = message;
            feedbackElement.className = `feedback show ${type}`;
            
            // Hide feedback after 10 seconds
            setTimeout(() => {
                feedbackElement.className = 'feedback hide';
            }, 10000);
        }
        
        function resetExercise() {
            initializeExercise();
            showFeedback('Exercise reset! Try again to improve your score.', 'error');
        }
        
        function showHint() {
            const hints = [
                "💡 Addition words (like 'furthermore', 'moreover') add extra information to support your point.",
                "💡 Equation words (like 'similarly', 'likewise') compare things or show they are the same.",
                "💡 Conclusion words (like 'therefore', 'in conclusion') wrap up your argument or paragraph.",
                "💡 'Thus' and 'therefore' indicate a logical conclusion from previous statements.",
                "💡 'Correspondingly' and 'equally' show that two things are similar or balanced."
            ];
            
            const randomHint = hints[Math.floor(Math.random() * hints.length)];
            showFeedback(randomHint, 'success');
        }
    </script>
</body>
</html>
'''

# Save the HTML file
with open('ielts_vocabulary_exercise.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Interactive IELTS Vocabulary Exercise created successfully!")
print("📁 File saved as: ielts_vocabulary_exercise.html")
print("\n🎯 Features included:")
print("• Drag and drop interface")
print("• Real-time scoring and progress tracking")
print("• Immediate visual feedback (green for correct, red for incorrect)")
print("• Hint system with IELTS-specific guidance")
print("• Reset functionality")
print("• Mobile-responsive design")
print("• Band 7.5+ vocabulary tips in feedback")
print("\n📖 Exercise covers 24 essential IELTS linking words for:")
print("• Addition (10 words)")
print("• Equation/Similarity (5 words)")  
print("• Conclusion (9 words)")