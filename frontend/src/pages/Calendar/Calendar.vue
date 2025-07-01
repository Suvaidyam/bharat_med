<template>
	<div class="min-h-screen bg-gray-50 p-4 lg:p-6">
		<!-- Header -->
		<div class="mb-6">
			<div class="flex flex-col lg:flex-row lg:items-center lg:justify-between">
				<h1 class="text-2xl lg:text-3xl font-bold text-gray-900 mb-4 lg:mb-0">Calendar</h1>
				<div class="flex items-center space-x-3">
					<button
						@click="showAddEventModal = true"
						class="flex items-center px-4 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition-colors"
					>
						<svg
							class="w-4 h-4 mr-2"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M12 6v6m0 0v6m0-6h6m-6 0H6"
							/>
						</svg>
						Add Event
					</button>
					<button
						class="flex items-center px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
					>
						<svg
							class="w-4 h-4 mr-2"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"
							/>
						</svg>
						Filter
					</button>
				</div>
			</div>
		</div>

		<!-- Calendar Navigation -->
		<div class="bg-white rounded-xl shadow-sm border mb-6">
			<div class="p-4 lg:p-6">
				<div class="flex flex-col lg:flex-row lg:items-center lg:justify-between">
					<!-- Month Navigation -->
					<div class="flex items-center space-x-4 mb-4 lg:mb-0">
						<button
							@click="previousMonth"
							class="p-2 hover:bg-gray-100 rounded-lg transition-colors"
						>
							<svg
								class="w-5 h-5 text-gray-600"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M15 19l-7-7 7-7"
								/>
							</svg>
						</button>
						<button
							@click="goToToday"
							class="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors text-sm font-medium"
						>
							Today
						</button>
						<button
							@click="nextMonth"
							class="p-2 hover:bg-gray-100 rounded-lg transition-colors"
						>
							<svg
								class="w-5 h-5 text-gray-600"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M9 5l7 7-7 7"
								/>
							</svg>
						</button>
						<h2 class="text-lg font-semibold text-gray-900">{{ monthYear }}</h2>
					</div>

					<!-- View Toggle -->
					<div class="flex items-center bg-gray-100 rounded-lg p-1">
						<button
							v-for="view in views"
							:key="view.id"
							@click="currentView = view.id"
							:class="[
								'px-3 py-1.5 text-sm font-medium rounded-md transition-colors',
								currentView === view.id
									? 'bg-white text-gray-900 shadow-sm'
									: 'text-gray-600 hover:text-gray-900',
							]"
						>
							{{ view.name }}
						</button>
					</div>
				</div>
			</div>

			<!-- Calendar Grid -->
			<div class="border-t border-gray-200">
				<!-- Day Headers -->
				<div class="grid grid-cols-7 border-b border-gray-200">
					<div
						v-for="day in dayHeaders"
						:key="day"
						class="p-3 text-center text-sm font-medium text-gray-500 bg-gray-50"
					>
						{{ day }}
					</div>
				</div>

				<!-- Calendar Days -->
				<div class="grid grid-cols-7">
					<div
						v-for="day in calendarDays"
						:key="day.date"
						:class="[
							'min-h-24 lg:min-h-32 border-r border-b border-gray-200 p-2 lg:p-3',
							!day.currentMonth ? 'bg-gray-50' : 'bg-white',
							day.isToday ? 'bg-blue-50' : '',
						]"
					>
						<div class="flex justify-between items-start mb-2">
							<span
								:class="[
									'text-sm font-medium',
									!day.currentMonth ? 'text-gray-400' : 'text-gray-900',
									day.isToday ? 'text-blue-600' : '',
								]"
							>
								{{ day.day }}
							</span>
						</div>

						<!-- Events -->
						<div class="space-y-1">
							<div
								v-for="event in day.events"
								:key="event.id"
								@click="openEvent(event)"
								:class="[
									'text-xs px-2 py-1 rounded cursor-pointer truncate',
									getEventColor(event.type),
								]"
								:title="event.title"
							>
								{{ event.time }} - {{ event.title }}
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<!-- Add Event Modal -->
		<div
			v-if="showAddEventModal"
			class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50"
			@click="closeModal"
		>
			<div class="bg-white rounded-xl p-6 w-full max-w-md" @click.stop>
				<div class="flex justify-between items-center mb-4">
					<h3 class="text-lg font-semibold text-gray-900">Add New Event</h3>
					<button @click="closeModal" class="p-1 hover:bg-gray-100 rounded">
						<svg
							class="w-5 h-5 text-gray-400"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M6 18L18 6M6 6l12 12"
							/>
						</svg>
					</button>
				</div>

				<form @submit.prevent="addEvent" class="space-y-4">
					<div>
						<label class="block text-sm font-medium text-gray-700 mb-1"
							>Event Title</label
						>
						<input
							v-model="newEvent.title"
							type="text"
							required
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							placeholder="Enter event title"
						/>
					</div>

					<div class="grid grid-cols-2 gap-4">
						<div>
							<label class="block text-sm font-medium text-gray-700 mb-1"
								>Date</label
							>
							<input
								v-model="newEvent.date"
								type="date"
								required
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							/>
						</div>
						<div>
							<label class="block text-sm font-medium text-gray-700 mb-1"
								>Time</label
							>
							<input
								v-model="newEvent.time"
								type="time"
								required
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							/>
						</div>
					</div>

					<div>
						<label class="block text-sm font-medium text-gray-700 mb-1"
							>Event Type</label
						>
						<select
							v-model="newEvent.type"
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
						>
							<option value="meeting">Meeting</option>
							<option value="appointment">Appointment</option>
							<option value="training">Training</option>
							<option value="holiday">Holiday</option>
							<option value="other">Other</option>
						</select>
					</div>

					<div>
						<label class="block text-sm font-medium text-gray-700 mb-1"
							>Description (Optional)</label
						>
						<textarea
							v-model="newEvent.description"
							rows="3"
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							placeholder="Event description..."
						></textarea>
					</div>

					<div class="flex space-x-3 pt-4">
						<button
							type="submit"
							class="flex-1 bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors"
						>
							Add Event
						</button>
						<button
							type="button"
							@click="closeModal"
							class="flex-1 border border-gray-300 text-gray-700 py-2 px-4 rounded-lg hover:bg-gray-50 transition-colors"
						>
							Cancel
						</button>
					</div>
				</form>
			</div>
		</div>

		<!-- Event Details Modal -->
		<div
			v-if="selectedEvent"
			class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50"
			@click="selectedEvent = null"
		>
			<div class="bg-white rounded-xl p-6 w-full max-w-md" @click.stop>
				<div class="flex justify-between items-center mb-4">
					<h3 class="text-lg font-semibold text-gray-900">Event Details</h3>
					<button @click="selectedEvent = null" class="p-1 hover:bg-gray-100 rounded">
						<svg
							class="w-5 h-5 text-gray-400"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M6 18L18 6M6 6l12 12"
							/>
						</svg>
					</button>
				</div>

				<div class="space-y-3">
					<div>
						<h4 class="font-medium text-gray-900">{{ selectedEvent.title }}</h4>
						<p class="text-sm text-gray-600">{{ selectedEvent.time }}</p>
					</div>
					<div v-if="selectedEvent.description">
						<h5 class="text-sm font-medium text-gray-700 mb-1">Description</h5>
						<p class="text-sm text-gray-600">{{ selectedEvent.description }}</p>
					</div>
					<div class="flex space-x-2 pt-4">
						<button
							@click="deleteEvent(selectedEvent.id)"
							class="px-4 py-2 text-red-600 border border-red-300 rounded-lg hover:bg-red-50 transition-colors"
						>
							Delete
						</button>
						<button
							@click="selectedEvent = null"
							class="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-colors"
						>
							Close
						</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const currentDate = ref(new Date())
const currentView = ref('Month')
const showAddEventModal = ref(false)
const selectedEvent = ref(null)

const views = [
	{ id: 'Month', name: 'Month' },
	{ id: 'Week', name: 'Week' },
	{ id: 'Day', name: 'Day' },
	{ id: 'List', name: 'List' },
]

const dayHeaders = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

const events = ref([
	{
		id: 1,
		title: "Doctor's Meeting",
		date: '2025-07-01',
		time: '09:00',
		type: 'meeting',
		description: 'Weekly team meeting',
	},
	{
		id: 2,
		title: 'Patient Appointment - John Doe',
		date: '2025-07-01',
		time: '14:00',
		type: 'appointment',
		description: 'Regular checkup',
	},
	{
		id: 3,
		title: 'Medical Supplies Inventory',
		date: '2025-07-02',
		time: '08:00',
		type: 'other',
		description: 'Monthly inventory check',
	},
	{
		id: 4,
		title: 'Staff Training',
		date: '2025-07-03',
		time: '13:00',
		type: 'training',
		description: 'Emergency procedures training',
	},
	{
		id: 5,
		title: 'Hospital Board Meeting',
		date: '2025-07-04',
		time: '15:00',
		type: 'meeting',
		description: 'Monthly board meeting',
	},
	{
		id: 6,
		title: 'Clinic Closed - Holiday',
		date: '2025-07-10',
		time: '00:00',
		type: 'holiday',
		description: 'Independence Day observed',
	},
])

const newEvent = ref({
	title: '',
	date: '',
	time: '',
	type: 'meeting',
	description: '',
})

const monthYear = computed(() => {
	return currentDate.value.toLocaleDateString('en-US', {
		month: 'long',
		year: 'numeric',
	})
})

const calendarDays = computed(() => {
	const year = currentDate.value.getFullYear()
	const month = currentDate.value.getMonth()

	const firstDay = new Date(year, month, 1)
	const lastDay = new Date(year, month + 1, 0)
	const daysInMonth = lastDay.getDate()
	const startingDayOfWeek = firstDay.getDay()

	const days = []
	const today = new Date()

	// Previous month days
	const prevMonth = new Date(year, month - 1, 0)
	for (let i = startingDayOfWeek - 1; i >= 0; i--) {
		const day = prevMonth.getDate() - i
		const date = new Date(year, month - 1, day)
		days.push({
			day,
			date: date.toISOString().split('T')[0],
			currentMonth: false,
			isToday: false,
			events: getEventsForDate(date.toISOString().split('T')[0]),
		})
	}

	// Current month days
	for (let day = 1; day <= daysInMonth; day++) {
		const date = new Date(year, month, day)
		const isToday = date.toDateString() === today.toDateString()
		days.push({
			day,
			date: date.toISOString().split('T')[0],
			currentMonth: true,
			isToday,
			events: getEventsForDate(date.toISOString().split('T')[0]),
		})
	}

	// Next month days
	const remainingCells = 42 - days.length
	for (let day = 1; day <= remainingCells; day++) {
		const date = new Date(year, month + 1, day)
		days.push({
			day,
			date: date.toISOString().split('T')[0],
			currentMonth: false,
			isToday: false,
			events: getEventsForDate(date.toISOString().split('T')[0]),
		})
	}

	return days
})

const getEventsForDate = (date) => {
	return events.value.filter((event) => event.date === date)
}

const getEventColor = (type) => {
	const colors = {
		meeting: 'bg-green-100 text-green-800',
		appointment: 'bg-blue-100 text-blue-800',
		training: 'bg-purple-100 text-purple-800',
		holiday: 'bg-red-100 text-red-800',
		other: 'bg-yellow-100 text-yellow-800',
	}
	return colors[type] || colors.other
}

const previousMonth = () => {
	currentDate.value = new Date(
		currentDate.value.getFullYear(),
		currentDate.value.getMonth() - 1,
		1,
	)
}

const nextMonth = () => {
	currentDate.value = new Date(
		currentDate.value.getFullYear(),
		currentDate.value.getMonth() + 1,
		1,
	)
}

const goToToday = () => {
	currentDate.value = new Date()
}

const closeModal = () => {
	showAddEventModal.value = false
	newEvent.value = {
		title: '',
		date: '',
		time: '',
		type: 'meeting',
		description: '',
	}
}

const addEvent = () => {
	const id = events.value.length + 1
	events.value.push({
		id,
		...newEvent.value,
	})
	closeModal()
}

const openEvent = (event) => {
	selectedEvent.value = event
}

const deleteEvent = (eventId) => {
	events.value = events.value.filter((event) => event.id !== eventId)
	selectedEvent.value = null
}

onMounted(() => {
	// Set default date for new events to today
	newEvent.value.date = new Date().toISOString().split('T')[0]
})
</script>
