<template>
	<div class="min-h-screen bg-gray-50">
		<!-- Header -->
		<div class="bg-white shadow-sm border-b px-4 py-4 md:px-6">
			<div class="flex items-center gap-3">
				<button class="p-2 hover:bg-gray-100 rounded-lg">
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
				<div>
					<h1 class="text-xl font-semibold text-gray-900">Doctor Schedule</h1>
					<p class="text-sm text-gray-600">
						Manage and view doctor schedules and appointments.
					</p>
				</div>
			</div>
		</div>

		<div class="flex flex-col lg:flex-row">
			<!-- Left Sidebar - Calendar -->
			<div class="lg:w-80 bg-white border-r border-gray-200 p-4 md:p-6">
				<h2 class="text-lg font-semibold text-gray-900 mb-4">Calendar</h2>
				<p class="text-sm text-gray-600 mb-6">Select a date to view schedules.</p>

				<!-- Calendar -->
				<div class="bg-white rounded-lg">
					<div class="flex items-center justify-between mb-4">
						<h3 class="font-medium text-gray-900">
							{{ currentMonth }} {{ currentYear }}
						</h3>
						<div class="flex gap-1">
							<button @click="previousMonth" class="p-1 hover:bg-gray-100 rounded">
								<svg
									class="w-4 h-4"
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
							<button @click="nextMonth" class="p-1 hover:bg-gray-100 rounded">
								<svg
									class="w-4 h-4"
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
						</div>
					</div>

					<!-- Calendar Grid -->
					<div
						class="grid grid-cols-7 gap-1 text-center text-xs font-medium text-gray-500 mb-2"
					>
						<div
							v-for="day in ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']"
							:key="day"
							class="py-2"
						>
							{{ day }}
						</div>
					</div>

					<div class="grid grid-cols-7 gap-1">
						<button
							v-for="date in calendarDates"
							:key="date.key"
							@click="selectDate(date)"
							:class="[
								'aspect-square flex items-center justify-center text-sm rounded-lg transition-colors',
								date.isCurrentMonth
									? 'text-gray-900 hover:bg-gray-100'
									: 'text-gray-400',
								date.isSelected ? 'bg-blue-600 text-white hover:bg-blue-700' : '',
								date.isToday && !date.isSelected
									? 'bg-blue-100 text-blue-600'
									: '',
							]"
						>
							{{ date.date }}
						</button>
					</div>
				</div>
			</div>

			<!-- Main Content -->
			<div class="flex-1 p-4 md:p-6">
				<!-- Schedule Header -->
				<div class="bg-white rounded-lg shadow-sm border border-gray-200 mb-6">
					<div class="px-4 py-3 border-b border-gray-200">
						<div
							class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4"
						>
							<!-- View Tabs -->
							<div class="flex bg-gray-100 rounded-lg p-1">
								<button
									v-for="view in ['Day', 'Week', 'Month', 'List']"
									:key="view"
									@click="currentView = view"
									:class="[
										'px-3 py-1.5 text-sm font-medium rounded-md transition-colors',
										currentView === view
											? 'bg-white text-gray-900 shadow-sm'
											: 'text-gray-600 hover:text-gray-900',
									]"
								>
									{{ view }}
								</button>
							</div>

							<!-- Date Navigation -->
							<div class="flex items-center gap-2">
								<button
									@click="previousDay"
									class="p-2 hover:bg-gray-100 rounded-lg"
								>
									<svg
										class="w-4 h-4"
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
								<span
									class="text-sm font-medium text-gray-900 min-w-[120px] text-center"
								>
									{{ formatSelectedDate }}
								</span>
								<button @click="nextDay" class="p-2 hover:bg-gray-100 rounded-lg">
									<svg
										class="w-4 h-4"
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
							</div>
						</div>
					</div>
				</div>

				<!-- Daily Schedule -->
				<div class="bg-white rounded-lg shadow-sm border border-gray-200">
					<div class="px-4 py-4 border-b border-gray-200">
						<h2 class="text-lg font-semibold text-gray-900">Daily Schedule</h2>
						<p class="text-sm text-gray-600 mt-1">
							Schedule for {{ formatSelectedDate }} • Dr. {{ doctorName }}
						</p>
					</div>

					<!-- Time Slots -->
					<div class="divide-y divide-gray-200">
						<div
							v-for="slot in timeSlots"
							:key="slot.time"
							class="px-4 py-4 flex items-center justify-between hover:bg-gray-50 transition-colors"
						>
							<div class="flex items-center gap-4">
								<span class="text-sm font-medium text-gray-900 w-16">{{
									slot.time
								}}</span>
								<div class="hidden sm:block w-px h-8 bg-gray-200"></div>
							</div>

							<div class="flex-1 flex items-center justify-between">
								<div class="flex-1">
									<span class="text-sm text-gray-500">{{ slot.status }}</span>
								</div>

								<button
									v-if="slot.status === 'No appointments'"
									class="text-sm text-blue-600 hover:text-blue-700 font-medium"
								>
									Add Appointment
								</button>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

// Reactive data
const currentDate = ref(new Date())
const selectedDate = ref(new Date())
const currentView = ref('Day')
const doctorName = ref('Lisa Patel')

// Time slots for the schedule
const timeSlots = ref([
	{ time: '9:00 AM', status: 'No appointments' },
	{ time: '10:00 AM', status: 'No appointments' },
	{ time: '11:00 AM', status: 'No appointments' },
	{ time: '12:00 PM', status: 'No appointments' },
	{ time: '1:00 PM', status: 'No appointments' },
	{ time: '2:00 PM', status: 'No appointments' },
	{ time: '3:00 PM', status: 'No appointments' },
	{ time: '4:00 PM', status: 'No appointments' },
	{ time: '5:00 PM', status: 'No appointments' },
])

// Computed properties
const currentMonth = computed(() => {
	return currentDate.value.toLocaleDateString('en-US', { month: 'long' })
})

const currentYear = computed(() => {
	return currentDate.value.getFullYear()
})

const formatSelectedDate = computed(() => {
	return selectedDate.value.toLocaleDateString('en-US', {
		month: 'long',
		day: 'numeric',
		year: 'numeric',
	})
})

const calendarDates = computed(() => {
	const year = currentDate.value.getFullYear()
	const month = currentDate.value.getMonth()

	// First day of the month
	const firstDay = new Date(year, month, 1)
	const lastDay = new Date(year, month + 1, 0)

	// Start from Sunday of the week containing the first day
	const startDate = new Date(firstDay)
	startDate.setDate(startDate.getDate() - startDate.getDay())

	const dates = []
	const today = new Date()

	// Generate 42 days (6 weeks)
	for (let i = 0; i < 42; i++) {
		const date = new Date(startDate)
		date.setDate(startDate.getDate() + i)

		const isCurrentMonth = date.getMonth() === month
		const isToday = date.toDateString() === today.toDateString()
		const isSelected = date.toDateString() === selectedDate.value.toDateString()

		dates.push({
			date: date.getDate(),
			fullDate: new Date(date),
			isCurrentMonth,
			isToday,
			isSelected,
			key: `${date.getFullYear()}-${date.getMonth()}-${date.getDate()}`,
		})
	}

	return dates
})

// Methods
const selectDate = (dateObj) => {
	selectedDate.value = new Date(dateObj.fullDate)
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

const previousDay = () => {
	const newDate = new Date(selectedDate.value)
	newDate.setDate(newDate.getDate() - 1)
	selectedDate.value = newDate
}

const nextDay = () => {
	const newDate = new Date(selectedDate.value)
	newDate.setDate(newDate.getDate() + 1)
	selectedDate.value = newDate
}

// Initialize
onMounted(() => {
	// Set selected date to today
	selectedDate.value = new Date()
	currentDate.value = new Date()
})
</script>
