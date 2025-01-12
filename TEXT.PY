

    <!-- Mobile App Header -->
<div class="sticky top-0 bg-white shadow-sm z-50">
    <div class="flex justify-between items-center p-4">
        <div class="text-xl font-bold text-primary">LearnMate</div>
        <button class="bg-primary text-white px-4 py-2 rounded-full text-sm">Premium</button>
    </div>
</div>

<!-- Main Content -->
<div class="container mx-auto px-4 pb-20">

    <!-- Home Section -->
    <div id="home-section" class="active-section">
        <div class="grid grid-cols-2 gap-4 my-4">
            <div class="bg-white p-4 rounded-xl shadow">
                <p class="text-sm text-gray-600">Study Hours</p>
                <p class="font-bold text-xl text-primary">4.5 hrs</p>
            </div>
            <div class="bg-white p-4 rounded-xl shadow">
                <p class="text-sm text-gray-600">Tasks Done</p>
                <p class="font-bold text-xl text-primary">8/10</p>
            </div>
        </div>

        <div class="space-y-4">
            <div class="bg-white p-4 rounded-xl shadow">
                <h3 class="font-semibold mb-2">Today's Schedule</h3>
                <div class="space-y-2">
                    <div class="flex justify-between items-center">
                        <span>Mathematics</span>
                        <span class="text-primary">9:00 AM</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>Science</span>
                        <span class="text-primary">11:00 AM</span>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Study Section -->
    <div id="study-section" class="inactive-section">
        <h2 class="text-xl font-bold my-4">Study Materials</h2>
        <div class="grid grid-cols-2 gap-4">
            <div class="bg-white p-4 rounded-xl shadow">
                <i class="bi bi-journal-text text-2xl text-primary"></i>
                <h3 class="font-semibold mt-2">Notes</h3>
            </div>
            <div class="bg-white p-4 rounded-xl shadow">
                <i class="bi bi-file-text text-2xl text-primary"></i>
                <h3 class="font-semibold mt-2">Sample Papers</h3>
            </div>
            <div class="bg-white p-4 rounded-xl shadow">
                <i class="bi bi-camera text-2xl text-primary"></i>
                <h3 class="font-semibold mt-2">Scanner</h3>
            </div>
            <div class="bg-white p-4 rounded-xl shadow">
                <i class="bi bi-robot text-2xl text-primary"></i>
                <h3 class="font-semibold mt-2">AI Tutor</h3>
            </div>
        </div>
    </div>

    <!-- Games Section -->
    <div id="games-section" class="inactive-section">
        <h2 class="text-xl font-bold my-4">Educational Games</h2>
        <div class="grid grid-cols-2 gap-4">
            <div class="bg-white p-4 rounded-xl shadow">
                <i class="bi bi-123 text-2xl text-primary"></i>
                <h3 class="font-semibold mt-2">Math Games</h3>
            </div>
            <div class="bg-white p-4 rounded-xl shadow">
                <i class="bi bi-translate text-2xl text-primary"></i>
                <h3 class="font-semibold mt-2">Language</h3>
            </div>
            <div class="bg-white p-4 rounded-xl shadow">
                <i class="bi bi-globe text-2xl text-primary"></i>
                <h3 class="font-semibold mt-2">GK Quiz</h3>
            </div>
            <div class="bg-white p-4 rounded-xl shadow">
                <i class="bi bi-puzzle text-2xl text-primary"></i>
                <h3 class="font-semibold mt-2">Brain Games</h3>
            </div>
        </div>
    </div>

    <!-- Profile Section -->
    <div id="profile-section" class="inactive-section">
        <div class="bg-white rounded-xl shadow p-4 mt-4">
            <div class="flex items-center space-x-4">
                <div class="w-16 h-16 bg-primary rounded-full flex items-center justify-center">
                    <i class="bi bi-person text-2xl text-white"></i>
                </div>
                <div>
                    <h3 class="font-bold">Student Name</h3>
                    <p class="text-sm text-gray-600">Class 10th</p>
                </div>
            </div>
            <div class="mt-4 space-y-2">
                <div class="flex justify-between items-center p-2 bg-gray-50 rounded">
                    <span>Progress</span>
                    <span class="text-primary">75%</span>
                </div>
                <div class="flex justify-between items-center p-2 bg-gray-50 rounded">
                    <span>Study Streak</span>
                    <span class="text-primary">5 days</span>
                </div>
            </div>
        </div>
    </div>

    <!-- Bottom Navigation -->
    <div class="fixed bottom-0 left-0 right-0 bg-white border-t flex justify-around py-3">
        <button onclick="showSection('home')" class="flex flex-col items-center">
            <i class="bi bi-house text-xl text-primary"></i>
            <span class="text-xs">Home</span>
        </button>
        <button onclick="showSection('study')" class="flex flex-col items-center">
            <i class="bi bi-book text-xl text-gray-600"></i>
            <span class="text-xs">Study</span>
        </button>
        <button onclick="showSection('games')" class="flex flex-col items-center">
            <i class="bi bi-controller text-xl text-gray-600"></i>
            <span class="text-xs">Games</span>
        </button>
        <button onclick="showSection('profile')" class="flex flex-col items-center">
            <i class="bi bi-person text-xl text-gray-600"></i>
            <span class="text-xs">Profile</span>
        </button>
    </div>
</div>

<script>
    function showSection(sectionName) {
        // Hide all sections
        document.getElementById('home-section').classList.add('inactive-section');
        document.getElementById('study-section').classList.add('inactive-section');
        document.getElementById('games-section').classList.add('inactive-section');
        document.getElementById('profile-section').classList.add('inactive-section');

        // Show selected section
        document.getElementById(`${sectionName}-section`).classList.remove('inactive-section');

        // Update navigation icons
        const icons = document.querySelectorAll('.bottom-0 i');
        icons.forEach(icon => icon.classList.remove('text-primary'));
        icons.forEach(icon => icon.classList.add('text-gray-600'));

        const activeIcon = document.querySelector(`button[onclick="showSection('${sectionName}')"] i`);
        activeIcon.classList.remove('text-gray-600');
        activeIcon.classList.add('text-primary');
    }

    // Check trial period
    const trialStartDate = localStorage.getItem('trialStartDate');
    if (!trialStartDate) {
        localStorage.setItem('trialStartDate', new Date().toISOString());
    }
</script>

</body>

</html> 