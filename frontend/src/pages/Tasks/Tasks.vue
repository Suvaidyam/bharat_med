<template>
	<div class="min-h-screen p-6">
		<div class="">
			<!-- Header -->
			<div class="flex items-center justify-between mb-6">
				<h1 class="text-2xl font-bold text-gray-900">Tasks</h1>
				<button
					class="bg-black text-white px-4 py-2 rounded-lg hover:bg-gray-800 transition-colors flex items-center gap-2"
				>
					<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M12 4v16m8-8H4"
						></path>
					</svg>
					Add Task
				</button>
			</div>

			<!-- Search and Filters -->
			<div class="flex flex-col sm:flex-row gap-4 mb-6">
				<div class="flex-1 relative">
					<svg
						class="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400"
						fill="none"
						stroke="currentColor"
						viewBox="0 0 24 24"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
						></path>
					</svg>
					<input
						v-model="searchQuery"
						type="text"
						placeholder="Search tasks..."
						class="w-full pl-10 pr-4 py-2 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
					/>
				</div>
				<div class="flex gap-2">
					<select
						v-model="statusFilter"
						class="px-4 py-2 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
					>
						<option value="">All Status</option>
						<option value="todo">To Do</option>
						<option value="in-progress">In Progress</option>
						<option value="completed">Completed</option>
					</select>
					<select
						v-model="priorityFilter"
						class="px-4 py-2 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
					>
						<option value="">All Priorities</option>
						<option value="high">High</option>
						<option value="medium">Medium</option>
						<option value="low">Low</option>
					</select>
					<button class="p-2 border border-gray-200 rounded-lg hover:bg-gray-50">
						<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M4 6h16M4 10h16M4 14h16M4 18h16"
							></path>
						</svg>
					</button>
					<button class="p-2 border border-gray-200 rounded-lg hover:bg-gray-50">
						<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"
							></path>
						</svg>
					</button>
				</div>
			</div>

			<!-- Task List -->
			<div class="bg-white rounded-xl shadow-sm border border-gray-200">
				<div class="p-6 border-b border-gray-200">
					<h2 class="text-lg font-semibold text-gray-900">Task List</h2>
					<p class="text-sm text-gray-500 mt-1">
						Manage your tasks and track progress • {{ filteredTasks.length }} tasks
					</p>
				</div>

				<div class="divide-y divide-gray-100">
					<div
						v-for="task in filteredTasks"
						:key="task.id"
						class="p-6 hover:bg-gray-50 transition-colors"
					>
						<div class="flex items-start gap-4">
							<!-- Drag Handle -->
							<div
								class="flex items-center justify-center w-4 h-6 text-gray-400 cursor-move"
							>
								<svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
									<path
										d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z"
									></path>
								</svg>
							</div>

							<!-- Checkbox -->
							<div class="flex items-center pt-1">
								<input
									type="checkbox"
									:checked="task.status === 'completed'"
									@change="toggleTaskStatus(task.id)"
									class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 focus:ring-2"
								/>
							</div>

							<!-- Task Content -->
							<div class="flex-1 min-w-0">
								<div class="flex items-start justify-between">
									<div class="flex-1">
										<div class="flex items-center gap-2 mb-1">
											<h3
												class="text-sm font-medium text-gray-900"
												:class="{
													'line-through text-gray-500':
														task.status === 'completed',
												}"
											>
												{{ task.title }}
											</h3>
											<span
												v-if="task.priority"
												:class="getPriorityClass(task.priority)"
												class="px-2 py-1 text-xs font-medium rounded-full"
											>
												{{ task.priority }}
											</span>
										</div>
										<p class="text-sm text-gray-600 mb-3">
											{{ task.description }}
										</p>

										<div class="flex items-center gap-4 text-xs text-gray-500">
											<div class="flex items-center gap-1">
												<div
													:class="getStatusIndicatorClass(task.status)"
													class="w-2 h-2 rounded-full"
												></div>
												<span class="capitalize">{{
													task.status.replace('-', ' ')
												}}</span>
											</div>
											<div class="flex items-center gap-1">
												<svg
													class="w-3 h-3"
													fill="none"
													stroke="currentColor"
													viewBox="0 0 24 24"
												>
													<path
														stroke-linecap="round"
														stroke-linejoin="round"
														stroke-width="2"
														d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
													></path>
												</svg>
												<span>Due: {{ formatDate(task.dueDate) }}</span>
											</div>
											<div class="flex items-center gap-1">
												<span>Assigned to: {{ task.assignee }}</span>
											</div>
										</div>
									</div>

									<!-- Action Buttons -->
									<div class="flex items-center gap-2 ml-4">
										<button
											class="p-1 text-gray-400 hover:text-gray-600 transition-colors"
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
													d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
												></path>
											</svg>
										</button>
										<button
											class="p-1 text-gray-400 hover:text-red-600 transition-colors"
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
													d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
												></path>
											</svg>
										</button>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue'

const searchQuery = ref('')
const statusFilter = ref('')
const priorityFilter = ref('')

const tasks = ref([
	{
		id: 1,
		title: 'Review patient records',
		description: 'Go through the latest patient records and update the system',
		priority: 'high',
		status: 'todo',
		dueDate: '2025-07-02',
		assignee: 'Dr. Sarah Johnson',
	},
	{
		id: 2,
		title: 'Order medical supplies',
		description: 'Check inventory and place orders for depleted items',
		priority: 'medium',
		status: 'in-progress',
		dueDate: '2025-07-03',
		assignee: 'Nurse Wilson',
	},
	{
		id: 3,
		title: 'Schedule staff meeting',
		description: 'Arrange monthly staff meeting and prepare agenda',
		priority: 'low',
		status: 'completed',
		dueDate: '2025-06-30',
		assignee: 'Admin Staff',
	},
	{
		id: 4,
		title: 'Update clinic protocols',
		description: 'Review and update clinic protocols based on new guidelines',
		priority: 'high',
		status: 'todo',
		dueDate: '2025-07-04',
		assignee: 'Dr. Sarah Johnson',
	},
	{
		id: 5,
		title: 'Follow up with patients',
		description: 'Call patients who had appointments last week for follow-up',
		priority: 'medium',
		status: 'in-progress',
		dueDate: '2025-07-02',
		assignee: 'Nurse Wilson',
	},
	{
		id: 6,
		title: 'Prepare monthly report',
		description: 'Compile statistics and prepare the monthly clinic performance report',
		priority: 'high',
		status: 'todo',
		dueDate: '2025-07-05',
		assignee: 'Dr. Sarah Johnson',
	},
])

const filteredTasks = computed(() => {
	return tasks.value.filter((task) => {
		const matchesSearch =
			task.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			task.description.toLowerCase().includes(searchQuery.value.toLowerCase())
		const matchesStatus = !statusFilter.value || task.status === statusFilter.value
		const matchesPriority = !priorityFilter.value || task.priority === priorityFilter.value

		return matchesSearch && matchesStatus && matchesPriority
	})
})

const getPriorityClass = (priority) => {
	const classes = {
		high: 'bg-red-100 text-red-800',
		medium: 'bg-yellow-100 text-yellow-800',
		low: 'bg-green-100 text-green-800',
	}
	return classes[priority] || 'bg-gray-100 text-gray-800'
}

const getStatusIndicatorClass = (status) => {
	const classes = {
		todo: 'bg-gray-400',
		'in-progress': 'bg-blue-400',
		completed: 'bg-green-400',
	}
	return classes[status] || 'bg-gray-400'
}

const formatDate = (dateString) => {
	const date = new Date(dateString)
	return date.toLocaleDateString('en-US', {
		month: 'short',
		day: 'numeric',
		year: 'numeric',
	})
}

const toggleTaskStatus = (taskId) => {
	const task = tasks.value.find((t) => t.id === taskId)
	if (task) {
		task.status = task.status === 'completed' ? 'todo' : 'completed'
	}
}
</script>
